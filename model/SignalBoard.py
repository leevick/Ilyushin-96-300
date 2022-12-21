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
from models import digHoleObj


class SignalBoard(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        board = add_cube((250e-4, 150e-4, 5e-3))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action='DESELECT')

        bm = bmesh.from_edit_mesh(board.data)
        for e in bm.edges:
            if math.fabs(e.verts[0].co.x - e.verts[1].co.x) < 1e-5 and math.fabs(e.verts[0].co.y - e.verts[1].co.y) < 1e-5:
                e.select_set(True)
        bpy.ops.transform.edge_bevelweight(value=1)

        bpy.ops.object.mode_set(mode='OBJECT')
        bpy.context.view_layer.objects.active = board
        bevel: bpy.types.BevelModifier = board.modifiers.new(
            type="BEVEL", name="bevel")
        bevel.affect = "EDGES"
        bevel.offset_type = "OFFSET"
        bevel.limit_method = "WEIGHT"
        bevel.width = 1e-3
        bevel.segments = 6
        bpy.ops.object.modifier_apply(modifier="bevel")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.uv.cube_project(scale_to_bounds=True)
        bpy.ops.object.mode_set(mode='OBJECT')

        cut = add_cube((220e-4, 120e-4, 1e-4), (0, 0, 25e-4))

        digHoleObj(board, cut)

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action="SELECT")

        bm = bmesh.from_edit_mesh(board.data)
        # for f in bm.faces:
        # if math.fabs(f.calc_area() -220e-4 * 120e-4) < 1e-5:

            # print(f.calc_area())
        # f.select_set(False)

        return board


argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


model: BlenderModel = SignalBoard()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
# model.render(argv[0])
