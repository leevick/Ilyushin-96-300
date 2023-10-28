from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder, extrudeFace
from blender_model import BlenderModel
from Materials import generatePureSignalLight
import bpy
import bmesh
import sys
import os
import math
import pathlib
import random

dir = pathlib.Path(__file__).parent.as_posix()
if not dir in sys.path:
    sys.path.append(dir)


signalHoles = [
    [325, 95, "green"],
    [325, 530, "green"],
    [160, 455, "green"],
    [490, 455, "green"],
    [240, 325, "yellow"],
    [410, 325, "yellow"],
    [325, 425, "yellow"],
    [325, 205, "yellow"],
]


class SPSH4(BlenderModel):

    def createPanelBackground(self) -> bpy.types.Material:
        index = bpy.data.materials.find("SPSH4")
        if index != -1:
            return bpy.data.materials[index]
        else:
            mat: bpy.types.Material = bpy.data.materials.new(name=f"SPSH4")
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
            paintRamp.color_ramp.elements[1].color = (0.021, 0.011, 0.011, 1)
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

            image = nodes.new("ShaderNodeTexImage")
            image.image = bpy.data.images.load(
                f"{os.getcwd()}/texture/SPSH4.png", check_existing=False)

            markMix: bpy.types.ShaderNodeMixRGB = nodes.new("ShaderNodeMixRGB")
            markMix.inputs["Color1"].default_value = (0, 0, 0, 1)
            links.new(image.outputs["Alpha"], markMix.inputs["Color2"])
            links.new(lessThan.outputs["Value"], markMix.inputs["Fac"])

            paintMix: bpy.types.ShaderNodeMixRGB = nodes.new(
                "ShaderNodeMixRGB")
            paintMix.inputs["Fac"].default_value = 0.5
            links.new(paintRamp.outputs["Color"], paintMix.inputs["Color1"])
            links.new(markMix.outputs["Color"], paintMix.inputs["Color2"])
            links.new(paintMix.outputs["Color"], nodes[0].inputs["Base Color"])

            return mat

    def create(self) -> bpy.types.Object:
        spsh4 = add_plane((65e-3, 65e-3))
        spsh4.data.materials.append(self.createPanelBackground())
        bevel(spsh4, 0.01625)
        bevel(spsh4, 1e-3, 3)
        extrudeFace(spsh4, 2e-3)
        spsh4.location = (0, 0, 1e-3)
        moveOrigin((0, 0, 0))

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action="DESELECT")
        bm = bmesh.from_edit_mesh(spsh4.data)
        for e in bm.edges:
            if e.verts[0].co.z > 5e-4 and e.verts[1].co.z > 5e-4:
                e.select_set(True)
        bpy.ops.transform.edge_bevelweight(value=1)

        bevelWeight(spsh4, 1e-3)

        # bpy.ops.object.shade_smooth()

        spsh4.data.materials.append(generatePureSignalLight((0, 1, 0, 1)))
        spsh4.data.materials.append(generatePureSignalLight((1, 1, 0, 1)))

        for h in signalHoles:
            cut = add_cylinder(2e-3, 3e-3, 3e-3)
            x = (h[0] - 325) * 1e-4
            y = (h[1] - 325) * -1e-4
            cut.location = (x, y, 1.5e-3)
            digHoleObj(spsh4, cut)

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action="DESELECT")

            bm = bmesh.from_edit_mesh(spsh4.data)
            for f in bm.faces:
                if math.fabs(f.calc_area() - (math.pi * 3e-3 * 3e-3)) < 1e-6:
                    centr = f.calc_center_median()
                    if math.fabs(centr.x - x) < 1e-6 and math.fabs(centr.y - y) < 1e-6:
                        f.select_set(True)
                        if h[2] == "green":
                            f.material_index = 1
                        else:
                            f.material_index = 2
            bpy.ops.uv.cube_project(scale_to_bounds=True)
            bpy.ops.object.mode_set(mode='OBJECT')

        return spsh4
