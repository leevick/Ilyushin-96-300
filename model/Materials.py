import bpy
import os
from io_scene_gltf2_msfs.blender.msfs_material_prop_update import MSFS_Material_Property_Update
from io_scene_gltf2_msfs.blender.msfs_material_function import MSFS_Material


def generateSignalBoardFrameMaterial() -> bpy.types.Material:
    index = bpy.data.materials.find("signalBoardFrame")
    if index != -1:
        return bpy.data.materials[index]
    else:
        sigFrame = bpy.data.materials.new(name="signalBoardFrame")
        sigFrame.use_nodes = True

        nodes = sigFrame.node_tree.nodes
        links = sigFrame.node_tree.links

        geometry: bpy.types.ShaderNodeNewGeometry = nodes.new(
            "ShaderNodeNewGeometry")
        noise: bpy.types.ShaderNodeTexNoise = nodes.new("ShaderNodeTexNoise")
        noise.inputs["Scale"].default_value = 892.1
        noise.inputs["Detail"].default_value = 15.0
        noise.inputs['Roughness'].default_value = 0.822

        links.new(geometry.outputs["Position"], noise.inputs["Vector"])

        invert: bpy.types.ShaderNodeInvert = nodes.new("ShaderNodeInvert")
        invert.inputs["Color"].default_value = (1, 1, 1, 1)

        links.new(noise.outputs["Fac"], invert.inputs["Fac"])
        links.new(noise.outputs["Fac"], nodes[0].inputs["Metallic"])
        links.new(invert.outputs["Color"], nodes[0].inputs["Roughness"])

        nodes[0].inputs["Base Color"].default_value = (0, 0, 0, 1)

        return sigFrame


def generateSignalBoardLightMaterial(name: str) -> bpy.types.Material:
    index = bpy.data.materials.find(f"signalBoardLight_{name}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        sigLight = bpy.data.materials.new(name=f"signalBoardLight_{name}")
        sigLight.use_nodes = True

        nodes = sigLight.node_tree.nodes
        links = sigLight.node_tree.links

        # Geometry Node
        geo: bpy.types.ShaderNodeNewGeometry = nodes.new(
            "ShaderNodeNewGeometry")

        # White Noise Node
        noise: bpy.types.ShaderNodeTexWhiteNoise = nodes.new(
            "ShaderNodeTexWhiteNoise")

        links.new(geo.outputs["Position"], noise.inputs["Vector"])

        # Gamma Node
        gamma: bpy.types.ShaderNodeGamma = nodes.new("ShaderNodeGamma")
        gamma.inputs["Gamma"].default_value = 5.0
        links.new(noise.outputs["Value"], gamma.inputs["Color"])

        # Map Range
        mapRange: bpy.types.ShaderNodeMapRange = nodes.new(
            "ShaderNodeMapRange")
        mapRange.inputs["To Max"].default_value = 0.1
        links.new(gamma.outputs["Color"], mapRange.inputs["Value"])
        links.new(mapRange.outputs["Result"], nodes[0].inputs["Base Color"])

        # Emission
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}.png", check_existing=False)
        links.new(nodeImage.outputs["Color"], nodes[0].inputs["Emission"])
        nodes[0].inputs["Emission Strength"].default_value = 10.0

        return sigLight


def generateColorBump(color) -> bpy.types.Material:
    index = bpy.data.materials.find(f"color_bump_{hash(color)}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"color_bump_{hash(color)}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 0.9
        nodes[0].inputs['Specular'].default_value = 0.1
        nodes[0].inputs['Metallic'].default_value = 0.8
        nodes[0].inputs['Base Color'].default_value = color

        return matFace


def generateClockGlass(color=(1, 1, 1, 0.001)) -> bpy.types.Material:
    index = bpy.data.materials.find(f"clock_glass_{hash(color)}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        # Create glass material
        matGlass = bpy.data.materials.new(name=f"clock_glass_{hash(color)}")
        matGlass.use_nodes = True
        matGlass.msfs_material_type = "msfs_glass"
        matGlass.msfs_base_color_factor = color
        matGlass.msfs_roughness_factor = 0.05
        msfs_mat = MSFS_Material(matGlass)

        MSFS_Material_Property_Update.update_msfs_material_type(
            matGlass, bpy.context)

        return matGlass


def generateScreenGauge(name: str) -> bpy.types.Material:
    index = bpy.data.materials.find(f"$SCREEN_{name.upper()}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        # Create glass material
        matGlass = bpy.data.materials.new(name=f"$SCREEN_{name.upper()}")
        matGlass.use_nodes = True
        matGlass.msfs_material_type = "msfs_standard"
        matGlass.msfs_base_color_factor = (0, 0, 0, 1)
        matGlass.msfs_metallic_factor = 0.0
        msfs_mat = MSFS_Material(matGlass)

        MSFS_Material_Property_Update.update_msfs_material_type(
            matGlass, bpy.context)

        return matGlass
