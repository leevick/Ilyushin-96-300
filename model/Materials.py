import bpy
import os


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
