import bpy
from models import BlenderModel
from utils import add_cube, subdivideEdges, moveEdges, add_plane, removeEdges, moveFaces, removeVertice, moveVertice, extrudeEdges, removeFaces
from Materials import panelWithPaints
from typing import List
import math


class LeftGlareshield(BlenderModel):

    height: float = 450e-4
    width: float
    depth: float

    lowerEdgeOffset: float = 1e-2
    lowerZOffset: float = 1e-2
    signalPanelOffset: float = 2e-2
    lowerEdgeSlope: float

    horizontalTicks: List[float] = [22.0, 152, 308.0]
    horizontalTotal: float = 414.0
    distToPU56: float

    shadeDepth: float = 3e-2
    distToWindow: float = 525e-3
    upperDepth: float = distToWindow / math.cos(math.radians(distToWindow))

    def __init__(self, width: float, depth: float, toPU56: float) -> None:
        super().__init__()
        self.width = width
        self.depth = depth
        self.lowerEdgeSlope = self.lowerEdgeOffset / \
            (self.depth / 2 - self.lowerZOffset)
        self.distToPU56 = toPU56

    def create(self) -> bpy.types.Object:

        # box
        box = add_cube((self.width, self.height, self.depth))
        subdivideEdges(box, lambda e: e.verts[0].co.x * e.verts[1].co.x <
                       0 and e.verts[0].co.z > 0
                       and e.verts[1].co.z > 0, 4)

        moveFaces(
            box, (-self.distToPU56, 0, 0), lambda f:
                f.normal.x > 0
        )

        removeVertice(box, lambda v: v.co.x < 0 and v.co.y > 0 and v.co.z < 0)

        moveVertice(box, (0, -self.height / 2, 0), lambda v: v.co.x <
                    -2 / 5 * self.width and v.co.y > 0 and v.co.z > 0)

        moveVertice(box, (-(self.horizontalTicks[2] / self.horizontalTotal - 4 / 5) * self.width, 0, 0), lambda v:
                    v.co.x < -1 / 4 * self.width
                    and v.co.x > -3 / 8 * self.width
                    and v.co.z > 0)

        moveVertice(box, (-((self.horizontalTicks[2] - 22) / self.horizontalTotal - 3 / 5) * self.width, 0, 0), lambda v:
                    v.co.x > -1 / 10 * self.width - 1e-3
                    and v.co.x < -1 / 10 * self.width + 1e-3
                    and v.co.z > 0)

        moveVertice(box, (-((self.horizontalTicks[1] + 22) / self.horizontalTotal - 2 / 5) * self.width, 0, 0), lambda v:
                    v.co.x > 1 / 10 * self.width - 1e-3
                    and v.co.x < 1 / 10 * self.width + 1e-3
                    and v.co.z > 0)

        moveVertice(box, (-(self.horizontalTicks[1] / self.horizontalTotal - 1 / 5) * self.width, 0, 0), lambda v:
                    v.co.x > 3 / 10 * self.width - 1e-3
                    and v.co.x < 3 / 10 * self.width + 1e-3
                    and v.co.z > 0)

        subdivideEdges(box, lambda e: e.verts[0].co.z * e.verts[1].co.z <
                       0 and e.verts[0].co.y < 0
                       and e.verts[1].co.y < 0)

        moveEdges(box, (0, -self.lowerEdgeOffset, self.lowerZOffset), lambda e: e.verts[0].co.x * e.verts[1].co.x <
                  0 and e.verts[0].co.y < 0
                  and e.verts[1].co.y < 0 and e.verts[0].co.z == 0.0 and e.verts[1].co.z == 0)

        moveFaces(box, (0, 0, -self.signalPanelOffset),
                  lambda f: math.fabs(f.calc_area() - ((self.horizontalTicks[2] - self.horizontalTicks[1] - 44) / self.horizontalTotal * self.width * self.height)) < 1e-6)

        moveEdges(box, (0, -self.lowerEdgeSlope * self.signalPanelOffset, 0), lambda e: math.fabs(e.calc_length() - (
            self.horizontalTicks[2] - self.horizontalTicks[1] - 44) / self.horizontalTotal * self.width) < 1e-6 and e.verts[0].co.y < 0)

        subdivideEdges(box, lambda e:
                       e.verts[0].co.x > self.width / 4
                       and e.verts[1].co.x > self.width / 4
                       and ((e.verts[0].co + e.verts[1].co) / 2).z > 0
                       and ((e.verts[0].co + e.verts[1].co) / 2).z < self.depth / 2 - 1e-3, 1)

        moveVertice(box, (0,
                          self.lowerEdgeSlope *
                          (1 / 4 * self.depth - self.lowerZOffset - 5e-3),
                          1 / 4 * self.depth - self.lowerZOffset - 5e-3), lambda v: v.co.y < - self.height / 2
                    and v.co.y > -self.height / 2 - self.lowerEdgeOffset + 1e-3
                    and v.co.x > self.width / 4)

        extrudeEdges(box, (self.distToPU56, 0, 0), lambda e:
                     e.verts[0].co.x > self.width / 4
                     and e.verts[1].co.x > self.width / 4
                     and ((e.verts[0].co + e.verts[1].co) / 2).z > self.depth / 4 + self.lowerZOffset
                     )

        subdivideEdges(box, lambda e:
                       math.fabs(e.calc_length() - (self.width - self.distToPU56)) < 1e-3, 2)

        moveEdges(box, ((self.width - self.distToPU56) / 3 - 1e-2, 0, 0), lambda e:
                  e.verts[0].co.z * e.verts[1].co.z < 0
                  and e.verts[0].co.x > 0
                  and e.verts[0].co.x < self.width / 4
                  )

        moveEdges(box, ((self.width - self.distToPU56) * 2 / 3 - 44e-2, 0, 0), lambda e:
                  e.verts[0].co.z * e.verts[1].co.z < 0
                  and e.verts[0].co.x < 0
                  and e.verts[0].co.x > - self.width / 4
                  )

        removeEdges(box, lambda e:
                    (e.verts[0].co.x + e.verts[1].co.x) / 2 > -self.width / 4
                    and (e.verts[0].co.x + e.verts[1].co.x) / 2 < self.width / 4
                    and e.verts[0].co.z < 0
                    and e.verts[1].co.z < 0)

        moveEdges(box, (0, - self.depth * self.lowerEdgeSlope, 0), lambda e:
                  (e.verts[0].co.x + e.verts[1].co.x) / 2 < -self.width / 4
                  and e.verts[0].co.z < 0
                  and e.verts[1].co.z < 0)

        shade = add_plane((self.width, self.shadeDepth + self.depth))
        shade.rotation_euler[0] = math.radians(90)
        subdivideEdges(
            shade, lambda e:
            e.verts[0].co.x * e.verts[1].co.x < 0, 2)
        moveVertice(shade, (0, -self.height, 0),
                    lambda v: v.co.x < -self.width / 4)

        moveVertice(shade, (-1 / 3 * self.width, -self.height / 2, 0),
                    lambda v: v.co.x > -self.width / 4 and v.co.x < 0)

        moveVertice(shade, (-(self.horizontalTicks[2] / self.horizontalTotal - 1 / 3) * self.width, 0, 0),
                    lambda v: v.co.x < self.width / 4 and v.co.x > 0)

        shade.location = (
            0, self.height / 2, self.shadeDepth / 2)
        shade.parent = box

        box.data.materials.append(panelWithPaints(
            name="leftGlareshield", texture=None))

        return box
