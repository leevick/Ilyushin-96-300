from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder, extrudeFace
from blender_model import BlenderModel
from Materials import generatePureSignalLight, ironWithPaints
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


signalHoles = [
    [325, 95, "green"],
    [325, 530, "green"],
    [160, 455, "green"],
    [490, 455, "green"],
    [240, 325, "yellow"],
    [410, 325, "yellow"],
    [325, 425, "yellow"],
    [325, 205, "yellow"],
]


class SPSH4(BlenderModel):

    def create(self) -> bpy.types.Object:
        spsh4 = add_plane((65e-3, 65e-3))

        spsh4.data.materials.append(ironWithPaints("SPSH4", "SPSH4"))
        bevel(spsh4, 0.01625)
        bevel(spsh4, 1e-3, 3)
        extrudeFace(spsh4, 2e-3)
        spsh4.location = (0, 0, 1e-3)
        moveOrigin((0, 0, 0))

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='EDGE')
        bpy.ops.mesh.select_all(action="DESELECT")
        bm = bmesh.from_edit_mesh(spsh4.data)
        for e in bm.edges:
            if e.verts[0].co.z > 5e-4 and e.verts[1].co.z > 5e-4:
                e.select_set(True)
        bpy.ops.transform.edge_bevelweight(value=1)

        bevelWeight(spsh4, 1e-3)

        # bpy.ops.object.shade_smooth()

        spsh4.data.materials.append(generatePureSignalLight((0, 1, 0, 1)))
        spsh4.data.materials.append(generatePureSignalLight((1, 1, 0, 1)))

        for h in signalHoles:
            cut = add_cylinder(2e-3, 2e-3, 2e-3)
            x = (h[0] - 325) * 1e-4
            y = (h[1] - 325) * -1e-4
            cut.location = (x, y, 1.5e-3)
            digHoleObj(spsh4, cut)

            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_mode(type='FACE')
            bpy.ops.mesh.select_all(action="DESELECT")

            bm = bmesh.from_edit_mesh(spsh4.data)
            for f in bm.faces:
                if math.fabs(f.calc_area() - (math.pi * 2e-3 * 2e-3)) < 1e-6:
                    centr = f.calc_center_median()
                    if math.fabs(centr.x - x) < 1e-6 and math.fabs(centr.y - y) < 1e-6:
                        f.select_set(True)
                        if h[2] == "green":
                            f.material_index = 1
                        else:
                            f.material_index = 2
            bpy.ops.uv.cube_project(scale_to_bounds=True)
            bpy.ops.object.mode_set(mode='OBJECT')

        return spsh4
