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

from models import BlenderModel, Nut, generateClockGlass, generateClockBase, generateClockFace, importSvg, generatePanelBackgroud
from Materials import panelWithPaints
from utils import moveOrigin


class VR30BP(BlenderModel):
    radius: float
    thickness: float
    depth: float
    glassPosition: float
    model: bpy.types.Object

    def __init__(self, radius=40e-3, thickness=3e-3, depth=10e-3, glassPosition=5e-3) -> None:
        super().__init__()
        self.radius = radius
        self.thickness = thickness
        self.depth = depth
        self.glassPosition = glassPosition

    def create(self) -> bpy.types.Object:

        # Create cut object
        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius - self.thickness, depth=self.depth + 2 * self.thickness, vertices=72, location=(0, 0, 0))

        cut = bpy.context.active_object

        # Create base

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius, depth=self.depth, vertices=72)
        base = bpy.context.active_object

        # Apply boolean

        boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
        boolean.object = cut
        boolean.operation = "DIFFERENCE"
        bpy.ops.object.modifier_apply(modifier="cut_ops")
        bpy.data.objects.remove(cut)
        base = bpy.context.active_object
        base.data.materials.append(generateClockBase())

        # Create glass

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius - self.thickness, depth=1e-3, vertices=72, location=(0, 0, self.depth / 2 - self.glassPosition))
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        # Create face

        bpy.ops.mesh.primitive_circle_add(
            radius=self.radius, fill_type="NGON", location=(0, 0, -self.depth / 2))
        face = bpy.context.active_object
        face.data.materials.append(generateClockFace("VR30BPTicks"))

        # Create needles

        needle = importSvg("US2NeedleShape")
        bpy.context.view_layer.objects.active = needle
        needle.select_set(True)
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='BOUNDS')
        needle.location = (0, 110e-4, 0)
        moveOrigin((0, 0, 0))
        needle.location = (0, 0, -self.depth / 2 + 1e-3)
        needle.data.materials.append(
            generatePanelBackgroud("US2Needle.png"))
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.cube_project(scale_to_bounds=True)
        bpy.ops.object.mode_set(mode='OBJECT')

        b = 17.8
        a = -10
        c = -170

        needle.animation_data_create()
        needle.animation_data.action = bpy.data.actions.new(
            name="IAS")
        fcurve = needle.animation_data.action.fcurves.new(
            data_path="rotation_euler", index=2
        )

        k1 = fcurve.keyframe_points.insert(
            frame=0,
            value=0
        )
        k1.interpolation = "LINEAR"

        for i in range(700):
            k2 = fcurve.keyframe_points.insert(
                frame=i + 100,
                value=-(math.sqrt(i + 100 - a) * b + c) / 180.0 * math.pi
            )
            k2.interpolation = "LINEAR"

        # Create Nails

        nails = [
            Nut().create(), Nut().create(), Nut().create(), Nut().create()]

        for i in range(2):
            for j in range(2):
                nails[2 * i +
                      j].location = (375e-4 if i == 1 else -375e-4, 365e-4 if j == 1 else -365e-4, self.depth / 2)
                nails[2 * i + j].rotation_euler[2] = random.uniform(0, math.pi)
                nails[2 * i +
                      j].data.materials.append(panelWithPaints("panelPure", None))

        face.parent = base
        needle.parent = base
        glass.parent = base
        for n in nails:
            n.parent = base

        bpy.ops.object.select_all(action="DESELECT")
        base.select_set(True)

        moveOrigin((0.0, 0, self.depth / 2))

        self.model = base

        return self.model
