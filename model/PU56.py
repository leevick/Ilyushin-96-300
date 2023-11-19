from utils import add_plane, add_cube, bevel, moveOrigin, digHoleObj, bevelWeight, add_cylinder, removeFaces, bevelEdges, removeEdges, extrudeAlongNorm, bevelVertices
from PU56Button import PU56Button
from PU56SpeedKnob import PU56SpeedKnob
from PU56HKnob import PU56HKnob
from SignalBoard import SignalBoard
from models import generateClockFace, extrudeFace, US2, digHole, digHoleObj, RMI, AGB, VBM, moveOrigin
from blender_model import BlenderModel
from Materials import panelWithPaints, ironWithPaints
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


rectHoleList = [
    [-0.163, 0.023, 0.0565, 0.02, 0.002, ""],
    [-0.089, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.007, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.124, 0.023, 0.0565, 0.02, 0.002, ""],
    [0.079, 0.027, 0.018, 0.018, 0.001, ""],
    [0.079, 0.007, 0.018, 0.018, 0.001, "PU56KZONA"],
    [0.079, -0.013, 0.018, 0.018, 0.001, "PU56POS"],
    [0.099, 0.007, 0.018, 0.018, 0.001, "PU56GNAV"],
    [0.099, -0.013, 0.018, 0.018, 0.001, "PU56ZPU"],
    [-0.065, -0.013, 0.018, 0.018, 0.001, "PU56VEIS"],
    [-0.045, -0.013, 0.018, 0.018, 0.001, "PU56VNAV"],
    [-0.126, -0.013, 0.018, 0.018, 0.001, "PU56ESHEL"],
    [0.025, -0.013, 0.018, 0.018, 0.001, "PU56VSKOR"],
    [0.195, 0.007, 0.018, 0.018, 0.001, "PU56AP"],
    [0.195, -0.013, 0.018, 0.018, 0.001, "PU56OTKLAP"],
    [-0.21, 0.027, 0.018, 0.018, 0.001, "PU56AT"],
    [-0.21, 0.007, 0.018, 0.018, 0.001, "PU56STAB"],
    [-0.21, -0.013, 0.018, 0.018, 0.001, "PU56OTKLAT"],
    [-0.19, -0.013, 0.018, 0.018, 0.001, "PU56SKOR"],
    [0.2215, -0.0125, 0.007, 0.014, 0.0035, ""],
    [-0.2285, -0.0125, 0.007, 0.014, 0.0035, ""],
    [-0.014, 0.025, 0.008, 0.05, 0, ""],

]


class PU56(BlenderModel):

    panelWidth: float = 470e-3
    panelHeight: float = 80e-3

    width: float = panelWidth + 2e-3
    height: float = panelHeight + 2e-3
    depth: float = 130e-3

    shadeDepth: float = 3e-2
    distToWindow: float = 525e-3
    upperDepth: float = distToWindow / math.cos(math.radians(distToWindow))

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        mcp = add_plane((self.panelWidth, self.panelHeight))
        mcp.data.materials.append(panelWithPaints("PU56", "PU56"))

        box = add_cube(
            (self.panelWidth, self.panelHeight / 2, self.depth), (0, 0, -self.depth / 2))

        removeEdges(box, lambda e: e.verts[0].co.y > 0 and e.verts[1].co.y >
                    0 and e.verts[0].co.x * e.verts[1].co.x < 0)

        bevelEdges(
            box, 3e-3, 6, lambda a:
            a.verts[0].co.y < 0
            and a.verts[1].co.y < 0
            and a.verts[0].co.z != a.verts[1].co.z)

        extrudeAlongNorm(box, 1e-3, lambda f: True)
        bpy.ops.object.shade_smooth()

        box.data.materials.append(ironWithPaints("mcpBox", None))
        box.location.y = - self.panelHeight / 4
        box.parent = mcp

        box = add_cube(
            (self.panelWidth, self.panelHeight / 2, self.shadeDepth + self.upperDepth), (0, 0, -(self.shadeDepth + self.upperDepth) / 2 + self.shadeDepth))

        removeEdges(box, lambda e: e.verts[0].co.y < 0 and e.verts[1].co.y <
                    0 and e.verts[0].co.x * e.verts[1].co.x < 0)

        bevelEdges(
            box, 3e-3, 6, lambda a:
            a.verts[0].co.y > 0
            and a.verts[1].co.y > 0
            and a.verts[0].co.z != a.verts[1].co.z)

        bevelVertices(box, 5e-3, 6, lambda a: a.co.y < 0 and a.co.z > 0)

        extrudeAlongNorm(box, 1e-3, lambda f: True)
        bpy.ops.object.shade_smooth()

        box.data.materials.append(ironWithPaints("mcpBox", None))
        box.location.y = self.panelHeight / 4
        box.parent = mcp

        knob = PU56SpeedKnob().create()
        knob.location = (-148.5e-3, -24e-3, 0)
        knob.parent = mcp

        hknob = PU56HKnob().create()
        hknob.location = (-850e-4, -240e-4, 0)
        hknob.parent = mcp

        bevel(mcp, 3e-3, 6)
        for hole in rectHoleList:
            cut = add_plane((hole[2], hole[3]))
            if hole[4] != 0:
                bevel(cut, hole[4], 3)
            extrudeFace(cut, depth=1)
            bpy.ops.transform.translate(
                value=(hole[0] + hole[2] / 2, hole[1] - hole[3] / 2, 0.5))
            digHoleObj(mcp, cut)
            if hole[5] != "":
                bu: bpy.types.Object = PU56Button(hole[5]).create()
                bu.location = (hole[0] + hole[2] / 2, hole[1] - hole[3] / 2, 0)
                bu.parent = mcp

        return mcp
