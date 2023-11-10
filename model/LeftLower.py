import bpy

from models import BlenderModel
from utils import add_plane
from Materials import panelWithPaints


class LeftLower(BlenderModel):
    width: float = 44e-2
    height: float = 10e-2

    def create(self) -> bpy.types.Object:
        panel = add_plane((self.width, self.height))
        panel.data.materials.append(panelWithPaints("LeftLower", texture=None))
        return panel
