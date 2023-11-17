import bpy
from models import BlenderModel
from utils import add_cube, subdivideEdges
from Materials import panelWithPaints


class LeftGlareshield(BlenderModel):

    height: float = 450e-4
    width: float
    depth: float

    def __init__(self, width: float, depth: float) -> None:
        super().__init__()
        self.width = width
        self.depth = depth

    def create(self) -> bpy.types.Object:
        box = add_cube((self.width, self.height, self.depth))

        subdivideEdges(box, lambda e: e.verts[0].co.z * e.verts[1].co.z <
                       0 and e.verts[0].co.y < 0
                       and e.verts[1].co.y < 0)

        box.data.materials.append(panelWithPaints(
            name="leftGlareshield", texture=None))

        return box
