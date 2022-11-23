import bpy
import sys


class BlenderModel:
    def __init__(self) -> None:
        pass

    def render(self) -> None:
        pass


class US2(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        pass


argv = sys.argv
argv = argv[argv.index("--")+1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


classModel = globals()[argv[0]]


model: BlenderModel = classModel()
model.render()
