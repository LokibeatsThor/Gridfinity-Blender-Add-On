import bpy

class VIEW3D_PT_gridfinity_panel(bpy.types.Panel):
    bl_label = "Gridfinity Tile Generator"
    bl_idname = "VIEW3D_PT_gridfinity_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Gridfinity'

    def draw(self, context):
        layout = self.layout
        scene = context.scene  

        layout.prop(scene, "gridfinity_use_magnets")
        layout.prop(scene, "gridfinity_columns")
        layout.prop(scene, "gridfinity_rows")
        layout.operator("mesh.add_gridfinity_base", text="Add Gridfinity Base")
        layout.separator()
        layout.label(text="Future Options Coming Soon...")


def register():
    bpy.types.Scene.gridfinity_use_magnets = bpy.props.BoolProperty(
        name="Include Magnet Holes",
        description="Add magnet holes to the base",
        default=False,
    )
    bpy.types.Scene.gridfinity_columns = bpy.props.IntProperty(
        name="Columns",
        description="Number of columns",
        default=1,
        min=1,
        max=50,
    )
    bpy.types.Scene.gridfinity_rows = bpy.props.IntProperty(
        name="Rows",
        description="Number of rows",
        default=1,
        min=1,
        max=50,
    )
    bpy.utils.register_class(VIEW3D_PT_gridfinity_panel)

def unregister():
    del bpy.types.Scene.gridfinity_use_magnets
    del bpy.types.Scene.gridfinity_columns
    del bpy.types.Scene.gridfinity_rows
    bpy.utils.unregister_class(VIEW3D_PT_gridfinity_panel)