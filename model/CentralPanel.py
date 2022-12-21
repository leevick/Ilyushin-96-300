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
from models import generateClockFace, extrudeFace, US2, digHole, digHoleObj, RMI, AGR, VBM, moveOrigin
from utils import add_plane


class CentralPanel(BlenderModel):

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        width = 1742
        height = 918
        scale = 2.2

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        bpy.ops.object.editmode_toggle()
        x, y, z = bpy.context.active_object.dimensions
        bpy.ops.transform.resize(
            value=(width * scale / 10000.0 / 2.0, height * scale / 10000.0 / 2.0, z), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        panel = bpy.context.active_object
        panel.data.materials.append(generateClockFace("CentralPanelBackgroud"))

        extrudeFace(panel, 0.001)

        us2_x = 51.25e-3 - width * scale / 10000.0 / 2
        us2_y = height * scale / 10000.0 / 2 - 66.25e-3

        us2: US2 = US2()
        digHole(panel, us2.radius, 1, (us2_x, us2_y, 0))
        us2.create()
        us2.model.location = (us2_x, us2_y, 0)

        # RMI Outline
        rmi = RMI()
        rmiOutline = rmi.createOutline()
        rmiOutline.location = (0.14188, 0.00598, 0)

        digHoleObj(panel, rmiOutline)

        rmiModel = rmi.create()
        rmiModel.location = (0.14188, 0.00598, 0)

        # AGR
        digHole(panel, 45e-3, 1, (-0.04292, 0.02598, 0))

        agr: bpy.types.Object = AGR().create()

        agr.location = (-0.04292, 0.02598, 0)

        # VBM
        # vbm : bpy.types.Object = VBM().create()
        vbm_outline: bpy.types.Object = VBM().createOutline()
        vbm_outline.location = (
            2465e-4 - width * 1.1 / 10000, height * 1.1 / 10000 - 650e-4, 0)
        digHoleObj(panel, vbm_outline)

        vbm: bpy.types.Object = VBM().create()
        vbm.location = (
            2465e-4 - width * 1.1 / 10000, height * 1.1 / 10000 - 650e-4, 0)

        bpy.ops.object.select_all(action="DESELECT")

        us2.model.parent = panel
        rmiModel.parent = panel
        agr.parent = panel
        vbm.parent = panel

        panel.select_set(True)

        moveOrigin((0.0, 0.0, 0.0))

        # panel.rotation_euler[0] = math.radians(90)
        # panel.rotation_euler[2] = math.radians(180)
        # panel.location = (0, -0.5, 0.7)

        return panel

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.2, 0.6),
                                  rotation=(math.atan(1 / 3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 100
        light.color = (1, 1, 1)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + name
        bpy.ops.render.render(write_still=True)

        pass


argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


model: BlenderModel = CentralPanel()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
model.render(argv[0])
