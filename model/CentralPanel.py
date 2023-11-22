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
from CentralRightPanel import CentralRightPanel
from Materials import panelWithPaints
from Monitor import Monitor
from VR30BP import VR30BP
from StabIndicator import StabIndicator
from LeftLower import LeftLower
from RightLower import RightLower
from PU56 import PU56
from LeftGlareshield import LeftGlareshield


class CentralPanel(BlenderModel):

    width: float = 1742 * 2.2 * 1e-4
    height: float = 918 * 2.2 * 1e-4

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        bpy.ops.object.editmode_toggle()
        x, y, z = bpy.context.active_object.dimensions
        bpy.ops.transform.resize(
            value=(self.width / 2.0, self.height / 2.0, z), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        panel = bpy.context.active_object
        panel.data.materials.append(
            panelWithPaints("CentralPanelBackgroud", "CentralPanelBackgroud"))

        extrudeFace(panel, 0.001)

        stab_x = 55.3e-3 - self.width / 2
        stab_y = self.height / 2 - 154.5e-3

        stab = StabIndicator().create()
        cut = add_cube((300e-4, 670e-4, 1), (stab_x, stab_y, 0))
        digHoleObj(panel, cut)
        stab.location = (stab_x, stab_y, 0)
        stab.parent = panel

        us2_x = 51.25e-3 - self.width / 2
        us2_y = self.height / 2 - 66.25e-3

        us2: US2 = US2()
        digHole(panel, us2.radius, 1, (us2_x, us2_y, 0))
        us2.create()
        us2.model.location = (us2_x, us2_y, 0)

        vr30bp_x = 245.6e-3 - self.width / 2
        vr30bp_y = self.height / 2 - 150.0e-3

        vr30bp: VR30BP = VR30BP()
        digHole(panel, us2.radius, 1, (vr30bp_x, vr30bp_y, 0))
        vr30bp.create()
        vr30bp.model.location = (vr30bp_x, vr30bp_y, 0)
        vr30bp.model.parent = panel

        # RMI Outline
        rmi = RMI()
        rmiOutline = rmi.createOutline()
        rmiOutline.location = (0.14188, 0.00598, 0)

        digHoleObj(panel, rmiOutline)

        rmiModel = rmi.create()
        rmiModel.location = (0.14188, 0.00598, 0)

        # AGB
        digHole(panel, 45e-3, 1, (-0.04292, 0.02598, 0))

        agb: bpy.types.Object = AGB().create()

        agb.location = (-0.04292, 0.02598, 0)

        # VBM
        # vbm : bpy.types.Object = VBM().create()
        vbm_outline: bpy.types.Object = VBM().createOutline()
        vbm_outline.location = (
            2465e-4 - self.width / 2, self.height / 2 - 650e-4, 0)
        digHoleObj(panel, vbm_outline)

        vbm: bpy.types.Object = VBM().create()
        vbm.location = (
            2465e-4 - self.width / 2, self.height / 2 - 650e-4, 0)

        # Stab Trims
        cut = add_cube((295e-4, 2 * 165e-4, 1), (205e-4 - self.width / 2,
                       self.height / 2 - 1545e-4, 0))
        digHoleObj(panel, cut)

        sigTrimUp = SignalBoard("StabTrimUp").create()
        sigTrimUp.location = (205e-4 - self.width / 2,
                              self.height / 2 - (1545e-4 - 165e-4 / 2), 0)
        sigTrimUp.parent = panel

        sigTrimDown = SignalBoard("StabTrimDown").create()
        sigTrimDown.location = (205e-4 - self.width / 2,
                                self.height / 2 - (1545e-4 + 165e-4 / 2), 0)
        sigTrimDown.parent = panel

        # Engine Signals

        cut = add_cube((295e-4 * 4, 165e-4 * 4, 1), (-1096.2e-4 +
                       2 * 295e-4, -320.2e-4 - 2 * 165e-4, 0))

        digHoleObj(panel, cut)

        signalTexts = ["EngineFailure", "EngineFailure", "EngineFailure", "EngineFailure",
                       "EngineFault", "EngineFault", "EngineFault", "EngineFault",
                       "ReverseOn", "ReverseOn", "ReverseOn", "ReverseOn",
                       "EngineSurge", "EngineSurge", "EngineSurge", "EngineSurge", ]

        for i in range(4):
            for j in range(4):
                sig = SignalBoard(signalTexts[i + 4 * j]).create()
                sig.location = (-1096.2e-4 + 0.5 * 295e-4 + i *
                                295e-4, -320.2e-4 - 0.5 * 165e-4 - j * 165e-4, 0)
                sig.parent = panel

        bpy.ops.object.select_all(action="DESELECT")

        us2.model.parent = panel
        rmiModel.parent = panel
        agb.parent = panel
        vbm.parent = panel

        # CENTRAL RIGHT
        cr: CentralRightPanel = CentralRightPanel()
        cr.model = cr.create()
        cr.model.location = (self.width / 2.0 + 1e-3,
                             self.height / 2.0, 0)
        cr.model.parent = panel

        # Monitors
        m1 = Monitor().create()
        m1.parent = panel
        m1.location = (- self.width / 2 +
                       1025e-4 + 10e-4, - self.height / 2 - 1160e-4, 0)
        m2 = Monitor().create()
        m2.parent = panel
        m2.location = (- self.width / 2 +
                       3075e-4 + 30e-4, - self.height / 2 - 1160e-4, 0)

        leftND: Monitor = Monitor()
        leftND.model = leftND.create()
        leftND.model.parent = panel
        leftND.model.location = (-self.width / 2 - 1025e-4 -
                                 10e-4, - self.height / 2, 0)

        leftPFD = Monitor().create()
        leftPFD.parent = panel
        leftPFD.location = (-self.width / 2 - 1025e-4 -
                            30e-4 - 2050e-4, - self.height / 2, 0)

        rightND: Monitor = Monitor()
        rightND.model = rightND.create()
        rightND.model.parent = panel
        rightND.model.location = (self.width / 2 + rightND.width / 2 +
                                  30e-4 + cr.width, - self.height / 2, 0)

        rightPFD: Monitor = Monitor()
        rightPFD.model = rightPFD.create()
        rightPFD.model.parent = panel
        rightPFD.model.location = (self.width / 2 + rightND.width +
                                   50e-4 + rightPFD.width / 2 + cr.width, - self.height / 2, 0)

        llp: LeftLower = LeftLower()
        llp.model = llp.create()
        llp.model.location = (-self.width / 2 -
                              llp.width / 2, -self.height / 2 - llp.height / 2 - leftND.height / 2, 0)
        llp.model.parent = panel

        rlp: RightLower = RightLower()
        rlp.model = rlp.create()
        rlp.model.location = (self.width / 2 +
                              rlp.width / 2 + cr.width + 30e-4,
                              -self.height / 2 - rlp.height / 2 - leftND.height / 2, 0)
        rlp.model.parent = panel

        panel.location = (-cr.width / 2 - 5e-4, 0, 0)

        panel.select_set(True)
        moveOrigin((0.0, 0.0, 0.0))

        pu56: PU56 = PU56()
        pu56.model = pu56.create()
        pu56.model.location = (0, self.height / 2 +
                               pu56.height / 2, pu56.depth)
        pu56.model.parent = panel

        # Left Glareshield
        lgs: LeftGlareshield = LeftGlareshield(
            width=60e-2 - (self.width +
                           cr.width - pu56.width) / 2.0,
            depth=pu56.depth, toPU56=(self.width + 1e-3 + cr.width - pu56.width) / 2)
        lgs.model = lgs.create()
        lgs.model.location = (-pu56.width / 2 - lgs.width /
                              2 - 1e-3, self.height / 2 + lgs.height / 2 - 5e-3, lgs.depth / 2)
        lgs.model.parent = panel

        panel.rotation_euler[0] = math.radians(75)
        panel.rotation_euler[2] = math.radians(180)
        panel.location = (0, -23.8648, 1.25448)

        return panel

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.5, 1.5),
                                  rotation=(math.atan(1 / 3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 3
        light.color = (1, 1, 0.5)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + name
        bpy.ops.render.render(write_still=True)

        pass
