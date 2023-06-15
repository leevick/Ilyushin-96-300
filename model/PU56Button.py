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


class PU56Button(BlenderModel):
    name = []
    depth: float = 2e-3

    def __init__(self, name=["", ""]) -> None:
        super().__init__()
        self.name = name

    def create(self) -> bpy.types.Object:
        button = add_plane((18e-3, 18e-3))
        bevel(button, 5e-4, 3)
        extrudeFace(button, depth=self.depth)
        bpy.ops.transform.translate(value=(0, 0, self.depth))
        moveOrigin((0, 0, 0))

        if len(self.name) == 1:
            cut = add_plane((17e-3, 17e-3))
            bevel(cut, 1e-3, 6)
            extrudeFace(cut, depth=2e-3)
            bpy.ops.transform.translate(value=(0, 0, self.depth + 1.8e-3))
            digHoleObj(button, cut)
        elif len(self.name) == 2:
            cut = add_plane((17e-3, 8e-3))
            bevel(cut, 1e-4)
            extrudeFace(cut, depth=2e-3)
            bpy.ops.transform.translate(value=(0, 4.5e-3, self.depth + 1.8e-3))
            digHoleObj(button, cut)
            cut = add_plane((17e-3, 8e-3))
            bevel(cut, 1e-4)
            extrudeFace(cut, depth=2e-3)
            bpy.ops.transform.translate(
                value=(0, -4.5e-3, self.depth + 1.8e-3))
            digHoleObj(button, cut)

        return button
