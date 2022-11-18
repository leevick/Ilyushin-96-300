#!/usr/bin/python3

from glob import glob


def configure(ctx):

    pass


def build(ctx):
    ctx.recurse("vectors")
