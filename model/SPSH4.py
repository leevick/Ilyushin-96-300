from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder
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


class SPSH4(BlenderModel):
    width: float = 470e-3
    height: float = 80e-3

    def create(self) -> bpy.types.Object:
        return super().create()