import bpy

class OBJECT_UL_render_check_slow(bpy.types.UIList):
    # Constants (flags)
    # Be careful not to shadow FILTER_ITEM!
    ## << 向左位移 就是等于1
    VGROUP_EMPTY = 1 << 0

    # Custom properties, saved with .blend file.
    use_filter_empty: bpy.props.BoolProperty(
        name="过滤空",
        default=False,
        options=set(),
        description="是否过滤空顶点组",
    )
    use_filter_empty_reverse: bpy.props.BoolProperty(
        name="反转空",
        default=False,
        options=set(),
        description="反转空过滤",
    )
    use_filter_name_reverse: bpy.props.BoolProperty(
        name="反转名称",
        default=False,
        options=set(),
        description="反转明称过滤",
    )

    # This allows us to have mutually exclusive options, which are also all disable-able!
    #这允许我们拥有互斥的选项，这些选项也都是可禁用的！
    def _gen_order_update(name1, name2):
        def _u(self, ctxt):
            if (getattr(self, name1)):
                setattr(self, name2, False)
        return _u
        
    use_order_name: bpy.props.BoolProperty(
        name="Name", default=False, options=set(),
        description="按名称对组进行排序（不区分大小写）",
        update=_gen_order_update("use_order_name", "use_order_importance"),
    )
    use_order_importance: bpy.props.BoolProperty(
        name="Importance",
        default=False,
        options=set(),
        description="按组在网格中的平均权量对组进行排序",
        update=_gen_order_update("use_order_importance", "use_order_name"),
    )
    use_filter_orderby_invert: bpy.props.BoolProperty(name='',default = False)

    # 常用绘图项函数.
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index, flt_flag):
        # 以防万一，我们这里不使用它!
        self.use_filter_invert = False

        # 断言（IsInstance（项目，BPY.Types.VertexGroup）
        vgroup = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            # 这里我们使用了一个新的过滤特性：它可以通过flt_标志将数据传递到绘图项目
            # 参数，它确切地包含在此项的筛选器列表中设置的筛选器项!
            # 在本例中，我们将显示灰色的空组.
            if flt_flag & self.VGROUP_EMPTY:
                col = layout.column()
                col.enabled = False
                col.alignment = 'LEFT'
                col.prop(vgroup, "name", text="", emboss=False, icon_value=icon)

            else:
                layout.prop(vgroup, "name", text="", emboss=False, icon_value=icon)
            icon = 'LOCKED' if vgroup.lock_weight else 'UNLOCKED'
            layout.prop(vgroup, "lock_weight", text="", icon=icon, emboss=False)


        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            if flt_flag & self.VGROUP_EMPTY:
                layout.enabled = False

            layout.label(text="", icon_value=icon)


    def draw_filter(self, context, layout):
        # Nothing much to say here, it's usual UI code...
        row = layout.row()

        subrow = row.row(align=True)
        subrow.prop(self, "filter_name", text="")
        icon = 'ZOOM_OUT' if self.use_filter_name_reverse else 'ZOOM_IN'
        subrow.prop(self, "use_filter_name_reverse", text="", icon=icon)

        subrow = row.row(align=True)
        subrow.prop(self, "use_filter_empty", toggle=True)
        icon = 'ZOOM_OUT' if self.use_filter_empty_reverse else 'ZOOM_IN'
        subrow.prop(self, "use_filter_empty_reverse", text="", icon=icon)

        row = layout.row(align=True)
        row.label(text="Order by:")
        row.prop(self, "use_order_name", toggle=True)
        row.prop(self, "use_order_importance", toggle=True)
        icon = 'TRIA_UP' if self.use_filter_orderby_invert else 'TRIA_DOWN'
        row.prop(self, "use_filter_orderby_invert", text="", icon=icon)

    def filter_items_empty_vgroups(self, context, vgroups):
        # This helper function checks vgroups to find out whether they are empty, and what's their average weights.
        # TODO: This should be RNA helper actually (a vgroup prop like "raw_data: ((vidx, vweight), etc.)").
        #       Too slow for python!
        obj_data = context.active_object.data
        ret = {vg.index: [True, 0.0] for vg in vgroups}
        if hasattr(obj_data, "vertices"):  # Mesh data
            if obj_data.is_editmode:
                import bmesh
                bm = bmesh.from_edit_mesh(obj_data)
                # only ever one deform weight layer
                dvert_lay = bm.verts.layers.deform.active
                fact = 1 / len(bm.verts)
                if dvert_lay:
                    for v in bm.verts:
                        for vg_idx, vg_weight in v[dvert_lay].items():
                            ret[vg_idx][0] = False
                            ret[vg_idx][1] += vg_weight * fact
            else:
                fact = 1 / len(obj_data.vertices)
                for v in obj_data.vertices:
                    for vg in v.groups:
                        ret[vg.group][0] = False
                        ret[vg.group][1] += vg.weight * fact
        elif hasattr(obj_data, "points"):  # Lattice data
            # XXX no access to lattice editdata?
            fact = 1 / len(obj_data.points)
            for v in obj_data.points:
                for vg in v.groups:
                    ret[vg.group][0] = False
                    ret[vg.group][1] += vg.weight * fact
        return ret

    def filter_items(self, context, data, propname):
        # This function gets the collection property (as the usual tuple (data, propname)), and must return two lists:
        # * The first one is for filtering, it must contain 32bit integers were self.bitflag_filter_item marks the
        #   matching item as filtered (i.e. to be shown), and 31 other bits are free for custom needs. Here we use the
        #   first one to mark VGROUP_EMPTY.
        # * The second one is for reordering, it must return a list containing the new indices of the items (which
        #   gives us a mapping org_idx -> new_idx).
        # Please note that the default UI_UL_list defines helper functions for common tasks (see its doc for more info).
        # If you do not make filtering and/or ordering, return empty list(s) (this will be more efficient than
        # returning full lists doing nothing!).
        vgroups = getattr(data, propname)
        helper_funcs = bpy.types.UI_UL_list

        # Default return values.
        flt_flags = []
        flt_neworder = []

        # Pre-compute of vgroups data, CPU-intensive. :/
        vgroups_empty = self.filter_items_empty_vgroups(context, vgroups)

        # Filtering by name
        if self.filter_name:
            flt_flags = helper_funcs.filter_items_by_name(self.filter_name, self.bitflag_filter_item, vgroups, "name",
                                                          reverse=self.use_filter_name_reverse)
        if not flt_flags:
            flt_flags = [self.bitflag_filter_item] * len(vgroups)

        # Filter by emptiness.
        for idx, vg in enumerate(vgroups):
            if vgroups_empty[vg.index][0]:
                flt_flags[idx] |= self.VGROUP_EMPTY
                if self.use_filter_empty and self.use_filter_empty_reverse:
                    flt_flags[idx] &= ~self.bitflag_filter_item
            elif self.use_filter_empty and not self.use_filter_empty_reverse:
                flt_flags[idx] &= ~self.bitflag_filter_item

        # Reorder by name or average weight.
        if self.use_order_name:
            flt_neworder = helper_funcs.sort_items_by_name(vgroups, "name")
        elif self.use_order_importance:
            _sort = [(idx, vgroups_empty[vg.index][1]) for idx, vg in enumerate(vgroups)]
            flt_neworder = helper_funcs.sort_items_helper(_sort, lambda e: e[1], True)

        return flt_flags, flt_neworder
