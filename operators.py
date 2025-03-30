import bpy
from bpy.types import Operator
from .gridfinity_mesh_data import (
    vertices_with_magnets,
    faces_with_magnets,
    vertices_without_magnets,
    faces_without_magnets,
)

class OBJECT_OT_add_gridfinity_base(bpy.types.Operator):
    bl_idname = "mesh.add_gridfinity_base"
    bl_label = "Add Gridfinity Base"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        use_magnet_holes = scene.gridfinity_use_magnets
        columns = scene.gridfinity_columns
        rows = scene.gridfinity_rows

        verts_single = vertices_with_magnets if use_magnet_holes else vertices_without_magnets
        faces_single = faces_with_magnets if use_magnet_holes else faces_without_magnets

        spacing = 42  # 42mm standard Gridfinity spacing
        all_verts = []
        all_faces = []
        vert_offset = 0

        for row in range(rows):
            for col in range(columns):
                x_offset = col * spacing
                y_offset = row * spacing

                
                transformed_verts = [(x + x_offset, y + y_offset, z) for (x, y, z) in verts_single]
                all_verts.extend(transformed_verts)

                
                for face in faces_single:
                    all_faces.append([index + vert_offset for index in face])

                vert_offset += len(verts_single)

        # Create the mesh object
        mesh = bpy.data.meshes.new("GridfinityBase")
        mesh.from_pydata(all_verts, [], all_faces)
        mesh.update()

        obj = bpy.data.objects.new("GridfinityBase", mesh)
        context.collection.objects.link(obj)
        context.view_layer.objects.active = obj
        obj.select_set(True)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJECT_OT_add_gridfinity_base)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_add_gridfinity_base)
