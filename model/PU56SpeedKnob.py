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

        return knob
