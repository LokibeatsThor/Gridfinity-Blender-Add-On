import bpy

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

def unregister():
    del bpy.types.Scene.gridfinity_use_magnets
    del bpy.types.Scene.gridfinity_columns
    del bpy.types.Scene.gridfinity_rows
