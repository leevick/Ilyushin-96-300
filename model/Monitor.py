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

from blender_model import BlenderModel
from models import generateClockFace, extrudeFace, US2, digHole, digHoleObj, RMI, AGB, VBM, moveOrigin
from SignalBoard import SignalBoard
from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight


class Monitor(BlenderModel):

    width: float = 2000e-4
    height: float = 2000e-4
    depth: float = 500e-4
    screenWidth: float = 16e-2
    screenHeight: float = 14e-2
    screenDepth: float = 5e-4
    screenRadius: float = 2e-3
    edge_bevel: float = 50e-4

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        monitor = add_cube(
            (self.width, self.height, self.depth))

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action="DESELECT")
        bm = bmesh.from_edit_mesh(monitor.data)
        for e in bm.edges:
            if not (e.verts[0].co.z < 0 and e.verts[1].co.z) < 0:
                e.select_set(True)
        bpy.ops.transform.edge_bevelweight(value=1)

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action="DESELECT")

        for f in bm.faces:
            if f.normal.z < 0:
                bm.faces.remove(f)

        bevelWeight(monitor, self.edge_bevel)

        monitor.location = (0, 0, -self.depth / 2)
        moveOrigin((0, 0, 0))

        cut = add_plane((self.screenWidth, self.screenHeight))
        bevel(cut, self.screenRadius, 6)
        extrudeFace(cut, 2 * self.screenDepth)
        cut.location = (0, 0, self.screenDepth)

        digHoleObj(monitor, cut)

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action="SELECT")
        bpy.ops.transform.edge_bevelweight(value=0)
        bpy.ops.mesh.select_all(action="DESELECT")

        bm = bmesh.from_edit_mesh(monitor.data)
        for e in bm.edges:
            if \
                    math.fabs(e.verts[0].co.z) < 1e-6 and\
                    math.fabs(e.verts[1].co.z) < 1e-6 and\
                    math.fabs(e.verts[0].co.x) < self.screenWidth / 2 + 1e-3 and\
                    math.fabs(e.verts[1].co.x) < self.screenWidth / 2 + 1e-3 and\
                    math.fabs(e.verts[0].co.y) < self.screenHeight / 2 + 1e-3 and\
                    math.fabs(e.verts[1].co.y) < self.screenHeight / 2 + 1e-3:
                e.select_set(True)
        bpy.ops.transform.resize(value=(1.05, 1.05, 1))
        bpy.ops.object.mode_set(mode='OBJECT')

        return monitor
