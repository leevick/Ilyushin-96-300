import bpy
import os
import hashlib
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


def generatePureSignalLight(color=(1.0, 1.0, 1.0, 1.0)) -> bpy.types.Material:
    sha = hashlib.sha256()
    sha.update(str(color).encode())
    index = bpy.data.materials.find(f"pureBordLight_{sha.hexdigest()}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        sigLight = bpy.data.materials.new(
            name=f"pureBordLight_{sha.hexdigest()}")
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
        nodes[0].inputs["Emission"].default_value = color
        nodes[0].inputs["Emission Strength"].default_value = 1.0

        return sigLight


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
        nodes[0].inputs["Emission Strength"].default_value = 1.0

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


def ironWithPaints(name: str, texture: str | None) -> bpy.types.Material:
    index = bpy.data.materials.find(name)
    if index != -1:
        return bpy.data.materials[index]
    else:
        mat: bpy.types.Material = bpy.data.materials.new(name=name)
        mat.use_nodes = True

        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        texCoord: bpy.types.ShaderNodeTexCoord = nodes.new(
            "ShaderNodeTexCoord")
        paintNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")
        mixtureNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")
        bumpNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")

        paintNoise.noise_dimensions = "2D"
        mixtureNoise.noise_dimensions = "2D"
        bumpNoise.noise_dimensions = "2D"

        links.new(texCoord.outputs["Object"],
                  paintNoise.inputs["Vector"])
        links.new(texCoord.outputs["Object"],
                  mixtureNoise.inputs["Vector"])
        links.new(texCoord.outputs["Object"],
                  bumpNoise.inputs["Vector"])

        paintNoise.inputs["Scale"].default_value = 4.0
        paintNoise.inputs["Detail"].default_value = 16.0
        paintNoise.inputs["Roughness"].default_value = 0.7

        bumpNoise.inputs["Scale"].default_value = 7
        bumpNoise.inputs["Detail"].default_value = 4.2
        bumpNoise.inputs["Roughness"].default_value = 0.728

        mixtureNoise.inputs["Scale"].default_value = 999.70
        mixtureNoise.inputs["Detail"].default_value = 15.0
        mixtureNoise.inputs["Roughness"].default_value = 1

        paintRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        paintRamp.color_ramp.elements[0].color = (0.005, 0.003, 0.003, 1)
        paintRamp.color_ramp.elements[0].position = (0.427)
        paintRamp.color_ramp.elements[1].color = (0.01, 0.006, 0.006, 1)
        paintRamp.color_ramp.elements[1].position = (0.615)
        links.new(paintNoise.outputs["Fac"], paintRamp.inputs["Fac"])

        roughtRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        roughtRamp.color_ramp.elements[0].color = (0.108, 0.108, 0.108, 1)
        roughtRamp.color_ramp.elements[0].position = (0)
        roughtRamp.color_ramp.elements[1].color = (1, 1, 1, 1)
        roughtRamp.color_ramp.elements[1].position = (0.018)
        links.new(paintRamp.outputs["Color"], roughtRamp.inputs["Fac"])
        links.new(roughtRamp.outputs["Color"],
                  nodes[0].inputs["Roughness"])

        metalRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        metalRamp.color_ramp.elements[0].color = (0, 0, 0, 1)
        metalRamp.color_ramp.elements[0].position = (0)
        metalRamp.color_ramp.elements[1].color = (0.296, 0.296, 0.296, 1)
        metalRamp.color_ramp.elements[1].position = (0.167)
        links.new(paintRamp.outputs["Color"], metalRamp.inputs["Fac"])
        links.new(metalRamp.outputs["Color"], nodes[0].inputs["Metallic"])

        bump: bpy.types.ShaderNodeBump = nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = 0.539
        bump.inputs["Distance"].default_value = 0.005
        links.new(bumpNoise.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], nodes[0].inputs["Normal"])

        lessThan: bpy.types.ShaderNodeMath = nodes.new("ShaderNodeMath")
        lessThan.operation = "LESS_THAN"
        lessThan.inputs[1].default_value = 0.500
        links.new(mixtureNoise.outputs["Fac"], lessThan.inputs["Value"])

        if texture != None:
            image = nodes.new("ShaderNodeTexImage")
            image.image = bpy.data.images.load(
                f"{os.getcwd()}/texture/{texture}.png", check_existing=False)

            markMix: bpy.types.ShaderNodeMixRGB = nodes.new("ShaderNodeMixRGB")
            markMix.inputs["Color1"].default_value = (0, 0, 0, 1)
            links.new(image.outputs["Alpha"], markMix.inputs["Color2"])
            links.new(lessThan.outputs["Value"], markMix.inputs["Fac"])

        paintMix: bpy.types.ShaderNodeMixRGB = nodes.new(
            "ShaderNodeMixRGB")
        paintMix.inputs["Fac"].default_value = 0.5
        links.new(paintRamp.outputs["Color"], paintMix.inputs["Color1"])
        if texture != None:
            links.new(markMix.outputs["Color"], paintMix.inputs["Color2"])
        else:
            paintMix.inputs["Color2"].default_value = (0, 0, 0, 1)
        links.new(paintMix.outputs["Color"], nodes[0].inputs["Base Color"])

        return mat


def panelWithPaints(name: str, texture: str | None) -> bpy.types.Material:
    index = bpy.data.materials.find(name)
    if index != -1:
        return bpy.data.materials[index]
    else:
        mat: bpy.types.Material = bpy.data.materials.new(name=name)
        mat.use_nodes = True

        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        texCoord: bpy.types.ShaderNodeTexCoord = nodes.new(
            "ShaderNodeTexCoord")
        paintNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")
        mixtureNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")
        bumpNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
            "ShaderNodeTexNoise")

        paintNoise.noise_dimensions = "2D"
        mixtureNoise.noise_dimensions = "2D"
        bumpNoise.noise_dimensions = "2D"

        links.new(texCoord.outputs["Object"],
                  paintNoise.inputs["Vector"])
        links.new(texCoord.outputs["Object"],
                  mixtureNoise.inputs["Vector"])
        links.new(texCoord.outputs["Object"],
                  bumpNoise.inputs["Vector"])

        paintNoise.inputs["Scale"].default_value = 4.0
        paintNoise.inputs["Detail"].default_value = 16.0
        paintNoise.inputs["Roughness"].default_value = 0.7

        bumpNoise.inputs["Scale"].default_value = 7
        bumpNoise.inputs["Detail"].default_value = 4.2
        bumpNoise.inputs["Roughness"].default_value = 0.728

        mixtureNoise.inputs["Scale"].default_value = 999.70
        mixtureNoise.inputs["Detail"].default_value = 15.0
        mixtureNoise.inputs["Roughness"].default_value = 1

        paintRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        paintRamp.color_ramp.elements[0].color = (0.074, 0.137, 0.155, 1)
        paintRamp.color_ramp.elements[0].position = (0.427)
        paintRamp.color_ramp.elements[1].color = (0.130, 0.258, 0.296, 1)
        paintRamp.color_ramp.elements[1].position = (0.615)
        links.new(paintNoise.outputs["Fac"], paintRamp.inputs["Fac"])

        roughtRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        roughtRamp.color_ramp.elements[0].color = (0.108, 0.108, 0.108, 1)
        roughtRamp.color_ramp.elements[0].position = (0.097)
        roughtRamp.color_ramp.elements[1].color = (1, 1, 1, 1)
        roughtRamp.color_ramp.elements[1].position = (0.212)
        links.new(paintRamp.outputs["Color"], roughtRamp.inputs["Fac"])
        links.new(roughtRamp.outputs["Color"],
                  nodes[0].inputs["Roughness"])

        metalRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
            "ShaderNodeValToRGB")
        metalRamp.color_ramp.elements[0].color = (0, 0, 0, 1)
        metalRamp.color_ramp.elements[0].position = (0)
        metalRamp.color_ramp.elements[1].color = (0.296, 0.296, 0.296, 1)
        metalRamp.color_ramp.elements[1].position = (0.167)
        links.new(paintRamp.outputs["Color"], metalRamp.inputs["Fac"])
        links.new(metalRamp.outputs["Color"], nodes[0].inputs["Metallic"])

        bump: bpy.types.ShaderNodeBump = nodes.new("ShaderNodeBump")
        bump.inputs["Strength"].default_value = 0.539
        bump.inputs["Distance"].default_value = 0.005
        links.new(bumpNoise.outputs["Fac"], bump.inputs["Height"])
        links.new(bump.outputs["Normal"], nodes[0].inputs["Normal"])

        lessThan: bpy.types.ShaderNodeMath = nodes.new("ShaderNodeMath")
        lessThan.operation = "LESS_THAN"
        lessThan.inputs[1].default_value = 0.500
        links.new(mixtureNoise.outputs["Fac"], lessThan.inputs["Value"])

        if texture != None:
            image = nodes.new("ShaderNodeTexImage")
            image.image = bpy.data.images.load(
                f"{os.getcwd()}/texture/{texture}.png", check_existing=False)

            markMix: bpy.types.ShaderNodeMixRGB = nodes.new("ShaderNodeMixRGB")
            markMix.inputs["Color1"].default_value = (0, 0, 0, 1)
            links.new(image.outputs["Alpha"], markMix.inputs["Color2"])
            links.new(lessThan.outputs["Value"], markMix.inputs["Fac"])

        paintMix: bpy.types.ShaderNodeMixRGB = nodes.new(
            "ShaderNodeMixRGB")
        paintMix.inputs["Fac"].default_value = 0.5
        links.new(paintRamp.outputs["Color"], paintMix.inputs["Color1"])
        if texture != None:
            links.new(markMix.outputs["Color"], paintMix.inputs["Color2"])
        else:
            paintMix.inputs["Color2"].default_value = (0, 0, 0, 1)
        links.new(paintMix.outputs["Color"], nodes[0].inputs["Base Color"])

        return mat
