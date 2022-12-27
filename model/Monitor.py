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
from utils import add_plane, add_cube


class Monitor(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        monitor = add_cube((20e-2, 20e-2, 1e-2))
        return monitor
