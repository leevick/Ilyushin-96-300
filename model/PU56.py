from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder
from PU56Button import PU56Button
from SignalBoard import SignalBoard
from models import generateClockFace, extrudeFace, US2, digHole, digHoleObj, RMI, AGB, VBM, moveOrigin
from blender_model import BlenderModel
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


rectHoleList = [
    [-0.163, 0.023, 0.0565, 0.02, 0.002, ""],
    [-0.089, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.007, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.124, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.079, 0.027, 0.018, 0.018, 0.001, ""],
    [0.079, 0.007, 0.018, 0.018, 0.001, "PU56KZONA"],
    [0.079, -0.013, 0.018, 0.018, 0.001, "PU56POS"],
    [0.099, 0.007, 0.018, 0.018, 0.001, "PU56GNAV"],
    [0.099, -0.013, 0.018, 0.018, 0.001, "PU56ZPU"],
    [-0.065, -0.013, 0.018, 0.018, 0.001, "PU56VEIS"],
    [-0.045, -0.013, 0.018, 0.018, 0.001, "PU56VNAV"],
    [-0.126, -0.013, 0.018, 0.018, 0.001, "PU56ESHEL"],
    [0.025, -0.013, 0.018, 0.018, 0.001, "PU56VSKOR"],
    [0.195, 0.007, 0.018, 0.018, 0.001, "PU56AP"],
    [0.195, -0.013, 0.018, 0.018, 0.001, "PU56OTKLAP"],
    [-0.21, 0.027, 0.018, 0.018, 0.001, "PU56AT"],
    [-0.21, 0.007, 0.018, 0.018, 0.001, "PU56STAB"],
    [-0.21, -0.013, 0.018, 0.018, 0.001, "PU56OTKLAT"],
    [-0.19, -0.013, 0.018, 0.018, 0.001, "PU56SKOR"],
    [0.2215, -0.0125, 0.007, 0.014, 0.0035, ""],
    [-0.2285, -0.0125, 0.007, 0.014, 0.0035, ""],
    [-0.014, 0.025, 0.008, 0.05, 0, ""],

]


class PU56(BlenderModel):

    width: float = 470e-3
    height: float = 80e-3

    def __init__(self) -> None:
        super().__init__()

    def createPanelBackground(self) -> bpy.types.Material:
        index = bpy.data.materials.find("PU56Panel")
        if index != -1:
            return bpy.data.materials[index]
        else:
            mat: bpy.types.Material = bpy.data.materials.new(name=f"PU56Panel")
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

            image = nodes.new("ShaderNodeTexImage")
            image.image = bpy.data.images.load(
                f"{os.getcwd()}/texture/PU56.png", check_existing=False)

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
        mcp = add_plane((self.width, self.height))
        mcp.data.materials.append(self.createPanelBackground())

        knob: bpy.types.Object = add_cylinder(1e-2, 9e-3, 11e-3, 6)
        bevel(knob, 1e-3, 3, "EDGES")
        moveOrigin((0, 0, -5e-3))
        knob.location = (-148.5e-3, -24e-3, 0)
        knob.parent = mcp

        bevel(mcp, 3e-3, 6)
        for hole in rectHoleList:
            cut = add_plane((hole[2], hole[3]))
            if hole[4] != 0:
                bevel(cut, hole[4], 3)
            extrudeFace(cut, depth=1)
            bpy.ops.transform.translate(
                value=(hole[0] + hole[2] / 2, hole[1] - hole[3] / 2, 0.5))
            digHoleObj(mcp, cut)
            if hole[5] != "":
                bu: bpy.types.Object = PU56Button(hole[5]).create()
                bu.location = (hole[0] + hole[2] / 2, hole[1] - hole[3] / 2, 0)
                bu.parent = mcp

        return mcp
