import bpy
import sys
import os
import math
import pathlib


def generateClockFace(name: str) -> bpy.types.Material:

    index = bpy.data.materials.find(f"face_{name}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"face_{name}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 0.21
        nodes[0].inputs['Specular'].default_value = 0.031
        nodes[0].inputs['Metallic'].default_value = 0.5
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}.png", check_existing=False)
        links.new(nodeImage.outputs["Color"], nodes[0].inputs["Base Color"])
        return matFace


def generateClockBase() -> bpy.types.Material:
    index = bpy.data.materials.find("clock_base")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matBase = bpy.data.materials.new(name="clock_base")
        matBase.use_nodes = True

        nodes = matBase.node_tree.nodes
        links = matBase.node_tree.links

        nodes[0].inputs['Base Color'].default_value = (0, 0, 0, 1)
        nodes[0].inputs['Roughness'].default_value = 0.21
        nodes[0].inputs['Specular'].default_value = 0.031
        nodes[0].inputs['Metallic'].default_value = 0.5

        bump = nodes.new("ShaderNodeBump")

        musgrave = nodes.new("ShaderNodeTexMusgrave")
        musgrave.inputs["Scale"].default_value = 47.3
        musgrave.inputs["Detail"].default_value = 15.0
        musgrave.inputs["Dimension"].default_value = 0.0

        links.new(bump.outputs['Normal'], nodes[0].inputs['Normal'])
        links.new(musgrave.outputs[0], bump.inputs[2])
        return matBase


def generateClockGlass() -> bpy.types.Material:
    index = bpy.data.materials.find("clock_glass")
    if index != -1:
        return bpy.data.materials[index]
    else:
        # Create glass material
        matGlass = bpy.data.materials.new(name="clock_glass")
        matGlass.use_nodes = True
        nodes = matGlass.node_tree.nodes
        links = matGlass.node_tree.links
        nodes[0].inputs['Base Color'].default_value = (1, 1, 1, 0)
        nodes[0].inputs['Transmission'].default_value = 1
        nodes[0].inputs['Roughness'].default_value = 0.01
        return matGlass


class BlenderModel:
    def __init__(self) -> None:
        pass

    def create(self) -> bpy.types.Object:
        pass

    def render(self) -> None:
        pass


class US2(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        radius = 40e-3
        thickness = 3e-3
        depth = 10e-3
        glassPosition = 5e-3

        # Create cut object
        bpy.ops.mesh.primitive_cylinder_add(
            radius=radius - thickness, depth=depth + 2 * thickness, vertices=72, location=(0, 0, 0))

        bpy.context.active_object.name = 'cut'
        cut = bpy.context.active_object

        # Create base

        bpy.ops.mesh.primitive_cylinder_add(
            radius=radius, depth=depth, vertices=72)
        bpy.context.active_object.name = 'base'
        base = bpy.context.active_object

        # Apply boolean

        boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
        boolean.object = cut
        boolean.operation = "DIFFERENCE"
        bpy.ops.object.modifier_apply(modifier="cut_ops")
        bpy.data.objects.remove(bpy.data.objects['cut'])
        base = bpy.context.active_object
        base.data.materials.append(generateClockBase())

        # Create glass

        bpy.ops.mesh.primitive_cylinder_add(
            radius=radius - thickness, depth=1e-3, vertices=72, location=(0, 0, depth / 2 - glassPosition))
        bpy.context.active_object.name = 'glass'
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        # Create face

        bpy.ops.mesh.primitive_circle_add(
            radius=radius, fill_type="NGON", location=(0, 0, -depth/2))
        face = bpy.context.active_object
        face.data.materials.append(generateClockFace(__class__.__name__))

        bpy.ops.object.select_all(action="DESELECT")

        face.select_set(True)
        base.select_set(True)
        glass.select_set(True)

        bpy.ops.object.join()
        bpy.context.active_object.name = "US2"

        return bpy.context.active_object

    def render(self) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.1, 0.3),
                                  rotation=(math.atan(1/3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 200
        light.color = (1, 1, 1)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix()+"/US2"
        bpy.ops.render.render(write_still=True)

        pass


argv = sys.argv
argv = argv[argv.index("--")+1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


classModel = globals()[argv[0]]


model: BlenderModel = classModel()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
model.render()
