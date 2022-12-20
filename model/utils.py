import bpy


def add_cube(dimension=(1, 1, 1), location=(0, 0, 0)) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cube_add(location=location)
    bpy.ops.object.editmode_toggle()
    x, y, z = bpy.context.active_object.dimensions
    bpy.ops.transform.resize(
        value=(dimension[0] / 2.0, dimension[1] / 2.0, dimension[2] / 2.0))
    bpy.ops.object.editmode_toggle()
    return bpy.context.active_object


def add_plane(dimension=(1, 1), location=(0, 0, 0)) -> bpy.types.Object:
    bpy.ops.mesh.primitive_plane_add(location=location)
    bpy.ops.object.editmode_toggle()
    x, y, z = bpy.context.active_object.dimensions
    bpy.ops.transform.resize(
        value=(dimension[0] / 2.0, dimension[1] / 2.0, z))
    bpy.ops.object.editmode_toggle()
    return bpy.context.active_object
