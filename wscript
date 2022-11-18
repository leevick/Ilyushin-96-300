#!/usr/bin/python3

from glob import glob


def configure(ctx):

    pass


def build(ctx):
    # print(glob("src/**").append('package.json'))
    # ctx(rule="BUILD_PATH='${TGT}' npx react-scripts build",
    #     src=glob("src/**").append('package.json'), target="dist")
