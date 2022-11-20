import bpy
import os
import math


radius = 40e-3
thickness = 3e-3
depth = 20e-3
glass = 5e-3

# Remove default

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius - thickness, depth=depth, vertices=36, location=(0, 0, depth / 2 + thickness))

bpy.context.active_object.name = 'cut'
cut = bpy.context.active_object

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius, depth=depth, vertices=36)
bpy.context.active_object.name = 'base'
base = bpy.context.active_object


boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
boolean.object = cut
boolean.operation = "DIFFERENCE"
bpy.ops.object.modifier_apply(modifier="cut_ops")
bpy.data.objects.remove(bpy.data.objects['cut'])

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius - thickness, depth=1e-3, vertices=36, location=(0, 0, depth / 2 - glass))
bpy.context.active_object.name = 'glass'
glass = bpy.context.active_object


bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{os.path.basename(__file__).split('.')[0]}.blend")

bpy.ops.object.camera_add(location=(0, -0.5, 0.5),
                          rotation=(45/180 * math.pi, 0, 0))
