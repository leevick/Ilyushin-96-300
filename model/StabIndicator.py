import sys
import pathlib


import bpy
import bmesh
import math
from blender_model import BlenderModel
from utils import add_cube, add_cylinder, add_plane, bevel, extrudeFace, digHoleObj, removeFaces

dir = pathlib.Path(__file__).parent.as_posix()
if not dir in sys.path:
    sys.path.append(dir)


class StabIndicator(BlenderModel):

    width: float = 300e-4
    heigh: float = 670e-4
    depth: float = 500e-4

    glassWidth: float = 200e-4
    glassHeight: float = 500e-4
    glassDepth: float = 5e-4
    glassBevel: float = 20e-4

    holeWidth: float = 160e-4
    holeHeight: float = 420e-4
    holeOffset: float = 10e-4

    wheelRadius: float = 330e-4
    wheelHeight: float = 120e-4
    wheelDepth: float = 10e-4

    def isBackCover(self, obj: bmesh.types.BMFace) -> bool:
        return obj.normal.z < 0 and math.fabs(obj.calc_area() - self.width * self.heigh) < 1e-6

    def create(self) -> bpy.types.Object:
        box = add_cube((self.width, self.heigh, self.depth),
                       (0, 0, -self.depth / 2))

        # Cut covering glass
        cut = add_plane((self.glassWidth, self.glassHeight),
                        (0, 0, self.glassDepth))
        bevel(cut, self.glassBevel, 3)
        extrudeFace(cut, 2 * self.glassDepth)
        digHoleObj(box, cut)

        # Remove Back Cover
        removeFaces(box, self.isBackCover)

        # Cut covering glass
        cut = add_cube((self.holeWidth, self.holeHeight, 1),
                       (self.holeOffset, 0, 0))
        digHoleObj(box, cut)

        # Cylinder

        cl = add_cylinder(h=self.wheelHeight,
                          r1=self.wheelRadius, r2=self.wheelRadius, segments=36)
        cl.location = (self.holeOffset + 2e-3, 0, -
                       self.wheelDepth - self.wheelRadius)

        cl.rotation_euler[1] = math.pi / 2

        return box
