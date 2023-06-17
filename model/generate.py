import bpy
import sys
import os
import pathlib

dir = pathlib.Path(__file__).parent.as_posix()
if not dir in sys.path:
    sys.path.append(dir)

from CentralPanel import CentralPanel
from SignalBoard import SignalBoard
from models import BlenderModel
from Monitor import Monitor
from PU56 import PU56
from PU56Button import PU56Button


argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


classModel = globals()[argv[0]]


model: BlenderModel = classModel()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
if argv[1] == "True":
    model.render(argv[0])
