#!/usr/bin/python3

from glob import glob
import platform


def configure(ctx):

    if platform.system() == "Darwin":
        ctx.env.BL = "/Applications/Blender.app/Contents/MacOS/Blender"
        ctx.env.INK = "/Applications/Inkscape.app/Contents/MacOS/inkscape"
    else:
        ctx.env.BL = "blender"
    pass


def build(ctx):
    ctx.recurse("vectors")
    ctx.add_group()
    ctx(rule="cp -r texture ../msfs/Ilyushin-96-300/PackageSources/SimObjects/Airplanes/uac-il-96-300/")
    ctx.recurse("model")
    ctx.add_group()
    ctx(rule=f"{ctx.env.BL} -b -P ../export_vc.py -- CentralPanel.blend ../msfs/Ilyushin-96-300/PackageSources/SimObjects/Airplanes/uac-il-96-300/model/vc",
        source=["CentralPanel.blend", "export_vc.py"])
    ctx.add_group()
