from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder, union
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


class PU56SpeedKnob(BlenderModel):

    knobRadius: float = 10e-3
    knobHeight: float = 10.5e-3
    baseRadius: float = 11e-3
    baseHeight: float = 1e-3

    def __init__(self) -> None:
        super().__init__()

    def createMaterial(self) -> bpy.types.Material:
        index = bpy.data.materials.find("PU56SpeedKnob")
        if index != -1:
            return bpy.data.materials[index]
        else:
            mat: bpy.types.Material = bpy.data.materials.new(
                name=f"PU56SpeedKnob")
            mat.use_nodes = True

            nodes = mat.node_tree.nodes
            links = mat.node_tree.links

            texCoord: bpy.types.ShaderNodeTexCoord = nodes.new(
                "ShaderNodeTexCoord")
            paintNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
                "ShaderNodeTexNoise")

            links.new(texCoord.outputs["Object"],
                      paintNoise.inputs["Vector"])

            paintNoise.inputs["Scale"].default_value = 5.0
            paintNoise.inputs["Detail"].default_value = 15.0
            paintNoise.inputs["Roughness"].default_value = 1.0

            roughtRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
                "ShaderNodeValToRGB")
            roughtRamp.color_ramp.elements[0].color = (0.5, 0.5, 0.5, 1)
            roughtRamp.color_ramp.elements[0].position = (0.355)
            roughtRamp.color_ramp.elements[1].color = (1, 1, 1, 1)
            roughtRamp.color_ramp.elements[1].position = (1.000)

            links.new(paintNoise.outputs["Color"], roughtRamp.inputs["Fac"])
            links.new(roughtRamp.outputs["Color"],
                      nodes[0].inputs["Roughness"])

            nodes[0].inputs["Metallic"].default_value = 0.5
            nodes[0].inputs["Specular"].default_value = 0.25
            nodes[0].inputs["Base Color"].default_value = (0, 0, 0, 1)

            return mat

    def create(self) -> bpy.types.Object:

        knobBase: bpy.types.Object = add_cylinder(
            self.baseHeight, self.baseRadius, self.baseRadius, 36)
        moveOrigin((0, 0, -self.baseHeight/2))
        knobBase.location = (0, 0, 0)

        knob: bpy.types.Object = add_cylinder(
            self.knobHeight, self.knobRadius, self.knobRadius, 6)
        # bevel(knob, 1e-3, 3, "EDGES")
        moveOrigin((0, 0, -self.knobHeight / 2))
        knob.location = (0, 0, 5e-4)

        knob = union(knob, knobBase)
        moveOrigin((0, 0, 0))

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action="DESELECT")
        bm = bmesh.from_edit_mesh(knob.data)
        for e in bm.edges:
            if ((e.verts[0].co.z + e.verts[1].co.z) / 2 > self.baseHeight) and ((e.verts[0].co.x/2 + e.verts[1].co.x/2) * (e.verts[0].co.x/2 + e.verts[1].co.x/2) + (e.verts[0].co.y/2 + e.verts[1].co.y/2) * (e.verts[0].co.y/2 + e.verts[1].co.y/2) < self.baseRadius * self.knobRadius):
                e.select_set(True)
            else:
                e.select_set(False)

        bpy.ops.transform.edge_bevelweight(value=1)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action="DESELECT")

        bevelWeight(knob, 1e-3, 3)
        bpy.ops.object.shade_smooth()

        knob.data.materials.append(self.createMaterial())

        return knob
