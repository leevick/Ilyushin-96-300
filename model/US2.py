import bpy
import os
import math
import pathlib


radius = 40e-3
thickness = 3e-3
depth = 30e-3
glassPosition = 5e-3

# Remove default

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])

# Create cut object

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius - thickness, depth=depth, vertices=36, location=(0, 0, depth / 2 + thickness))

bpy.context.active_object.name = 'cut'
cut = bpy.context.active_object

# Create base

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius, depth=depth, vertices=36)
bpy.context.active_object.name = 'base'
base = bpy.context.active_object

# Apply boolean

boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
boolean.object = cut
boolean.operation = "DIFFERENCE"
bpy.ops.object.modifier_apply(modifier="cut_ops")
bpy.data.objects.remove(bpy.data.objects['cut'])
base = bpy.context.active_object


# Create glass

bpy.ops.mesh.primitive_cylinder_add(
    radius=radius - thickness + 1e-3, depth=1e-3, vertices=36, location=(0, 0, depth / 2 - glassPosition))
bpy.context.active_object.name = 'glass'
glass = bpy.context.active_object

# Create glass material

matGlass = bpy.data.materials.new(name="glass")
matGlass.use_nodes = True

nodes = matGlass.node_tree.nodes
links = matGlass.node_tree.links
# output = nodes.new(type='ShaderNodeOutputMaterial')
# shader = nodes.new(type="ShaderNodeBsdfDiffuse")
nodes[0].inputs['Base Color'].default_value = (1, 1, 1, 0)
nodes[0].inputs['Transmission'].default_value = 1
nodes[0].inputs['Roughness'].default_value = 0.01

glass.data.materials.append(matGlass)


# Create base material

matBase = bpy.data.materials.new(name="baseMat")
matBase.use_nodes = True

nodes = matBase.node_tree.nodes
links = matBase.node_tree.links

nodes[0].inputs['Base Color'].default_value = (0, 0, 0, 1)
nodes[0].inputs['Roughness'].default_value = 0.8
nodes[0].inputs['Metallic'].default_value = 1.0

base.data.materials[0] = matBase

# Save file

bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{os.path.basename(__file__).split('.')[0]}.blend")

# Add render camera

bpy.ops.object.camera_add(location=(0, -0.06, 0.3),
                          rotation=(math.atan(0.2), 0, 0))
bpy.context.scene.camera = bpy.context.object

# Add render light

bpy.ops.object.light_add(
    location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
light = bpy.data.lights[0]
light.energy = 200
light.color = (1, 1, 0.3)

# Set GPU render

bpy.context.scene.render.engine = 'CYCLES'
bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
bpy.context.scene.cycles.device = "GPU"
bpy.context.preferences.addons["cycles"].preferences.get_devices()

bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix()+"/US2"
bpy.ops.render.render(write_still=True)
