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
from models import generateClockFace, extrudeFace, US2, digHole, digHoleObj, RMI, AGB, VBM, moveOrigin, importSvg
from SignalBoard import SignalBoard
from utils import add_plane, add_cube
from Materials import panelWithPaints
from utils import bevel
from SPSH4 import SPSH4


class CentralRightPanel(BlenderModel):

    sigTextures = ["GearOnPower", "SteerDevice1", "SteerDevice2"]
    sigBaseLocation = (357.5e-4, -322.5e-4, 0)
    width: float = 135e-3
    height: float = 430e-3

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        panel = add_plane((self.width, self.height),
                          (self.width / 2, -self.height / 2, 0))
        moveOrigin((0, 0, 0))
        panel.data.materials.append(
            panelWithPaints("CentralRightPanel", "CentralRightPanel"))

        extrudeFace(panel, 0.001)

        # screen
        cut = add_plane((1, 1), (-4700e-4, -7019.6e-4, 0.5))
        bevel(cut, 4e-3, 3)
        extrudeFace(cut, 1)
        digHoleObj(panel, cut)
        # Signals
        cut = add_cube((295e-4 * 3, 165e-4, 1), (652.5e-4, -322.5e-4, 0))
        digHoleObj(panel, cut)

        for i in range(3):
            signal = SignalBoard(self.sigTextures[i]).create()
            signal.location = (
                self.sigBaseLocation[0] + i * 295e-4, self.sigBaseLocation[1], self.sigBaseLocation[2])
            signal.parent = panel

        # SPSH4

        cut = add_plane((65e-3, 65e-3))
        bevel(cut, 0.01625)
        bevel(cut, 1e-3, 3)
        extrudeFace(cut, 1)
        cut.location = (365e-4, -840e-4, 0.5)

        digHoleObj(panel, cut)

        spsh4 = SPSH4().create()
        spsh4.location = (365e-4, -840e-4, 1e-3)
        spsh4.parent = panel

        return panel
