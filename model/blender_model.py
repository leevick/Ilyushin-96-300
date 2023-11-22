from __future__ import annotations
import bpy
import sys
import math
import pathlib
from typing import List

dir = pathlib.Path(__file__).parent.as_posix()
if not dir in sys.path:
    sys.path.append(dir)


class BlenderModel:
    model: bpy.types.Object
    children: List[BlenderModel]

    def __init__(self) -> None:
        pass

    def create(self) -> bpy.types.Object:
        pass

    def applyPre(self) -> None:
        pass

    def applyPost(self) -> None:
        pass

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.1, 0.3),
                                  rotation=(math.atan(1 / 3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 10
        light.color = (1, 1, 1)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + \
            name
        bpy.ops.render.render(write_still=True)

        pass
