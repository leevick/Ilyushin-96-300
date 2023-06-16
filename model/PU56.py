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


rectHoleList = [
    [-0.163, 0.023, 0.0565, 0.02, 0.002],
    [-0.089, 0.023, 0.0565, 0.02, 0.002],
    [0.007, 0.023, 0.0565, 0.02, 0.002],
    [0.124, 0.023, 0.0565, 0.02, 0.002],
    [0.079, 0.027, 0.018, 0.018, 0.001],
    [0.079, 0.007, 0.018, 0.018, 0.001],
    [0.079, -0.013, 0.018, 0.018, 0.001],
    [0.099, 0.007, 0.018, 0.018, 0.001],
    [0.099, -0.013, 0.018, 0.018, 0.001],
    [-0.065, -0.013, 0.018, 0.018, 0.001],
    [-0.045, -0.013, 0.018, 0.018, 0.001],
    [-0.126, -0.013, 0.018, 0.018, 0.001],
    [0.025, -0.013, 0.018, 0.018, 0.001],
    [0.195, 0.007, 0.018, 0.018, 0.001],
    [0.195, -0.013, 0.018, 0.018, 0.001],
    [-0.21, 0.027, 0.018, 0.018, 0.001],
    [-0.21, 0.007, 0.018, 0.018, 0.001],
    [-0.21, -0.013, 0.018, 0.018, 0.001],
    [-0.19, -0.013, 0.018, 0.018, 0.001],
    [0.2215, -0.0125, 0.007, 0.014, 0.0035],
    [-0.2285, -0.0125, 0.007, 0.014, 0.0035],
    [-0.014, 0.025, 0.008, 0.05, 0],

]


class PU56(BlenderModel):

    width: float = 470e-3
    height: float = 80e-3

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        mcp = add_plane((self.width, self.height))
        mcp.data.materials.append(generateClockFace('PU56'))
        bevel(mcp, 3e-3, 6)
        for hole in rectHoleList:
            cut = add_plane((hole[2], hole[3]))
            if hole[4] != 0:
                bevel(cut, hole[4], 3)
            extrudeFace(cut, depth=1)
            bpy.ops.transform.translate(
                value=(hole[0] + hole[2] / 2, hole[1] - hole[3] / 2, 0.5))
            digHoleObj(mcp, cut)

        return mcp
