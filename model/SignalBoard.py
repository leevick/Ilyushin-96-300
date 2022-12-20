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
from utils import add_cube


class SignalBoard(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        board = add_cube((260e-4, 160e-4, 5e-3))
        bm = bmesh.new()

        return bpy.context.active_object


argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


model: BlenderModel = SignalBoard()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
model.render(argv[0])
