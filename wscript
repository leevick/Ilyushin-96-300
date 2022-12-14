#!/usr/bin/python3

from glob import glob


def configure(ctx):

    pass


def build(ctx):
    ctx.recurse("vectors")
    ctx.add_group()
    ctx(rule="cp -r texture ../msfs/Ilyushin-96-300/PackageSources/SimObjects/Airplanes/uac-il-96-300/")
    ctx.recurse("model")
    ctx.add_group()
    ctx(rule="blender -b -P ../export_vc.py -- ${SRC} ../msfs/Ilyushin-96-300/PackageSources/SimObjects/Airplanes/uac-il-96-300/model/vc",source="CentralPanel.blend")
    ctx.add_group()
