import bpy
import os


bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])
bpy.ops.mesh.primitive_cylinder_add(radius=40e-3, depth=10e-3, vertices=36)
bpy.ops.wm.save_mainfile(filepath=f"{os.getcwd()}/{os.path.basename(__file__).split('.')[0]}.blend")

