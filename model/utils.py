import bpy
import bmesh
from typing import Callable
from mathutils import Vector


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


def add_cylinder(h: float = 1.0, r1: float = 1.0, r2: float = 1.0, segments: int = 32) -> bpy.types.Object:
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=segments, radius=r1, depth=h)
    obj = bpy.context.active_object

    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='DESELECT')

    bm = bmesh.from_edit_mesh(obj.data)

    for f in bm.faces:
        if f.normal.z < 0:
            f.select_set(True)
            break

    x, y, z = bpy.context.active_object.dimensions
    bpy.ops.transform.resize(
        value=(r2 / r1, r2 / r1, z))

    bmesh.update_edit_mesh(obj.data)
    bm.free()

    bpy.ops.object.editmode_toggle()
    return bpy.context.active_object


def moveOrigin(org):
    saved_location = bpy.context.scene.cursor.location.xyz
    bpy.context.scene.cursor.location = org
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location.xyz = saved_location


def bevel(obj: bpy.types.Object, width: float, segments: int = 1, mode="VERTICES") -> None:
    bpy.context.view_layer.objects.active = obj
    bevel: bpy.types.BevelModifier = obj.modifiers.new(
        type="BEVEL", name="bevel")
    bevel.affect = mode
    bevel.offset_type = "OFFSET"
    bevel.width = width
    bevel.segments = segments
    bpy.ops.object.modifier_apply(modifier="bevel")


def extrudeFace(obj: bpy.types.Object, depth=10e-3) -> None:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action='SELECT')

    bm = bmesh.new()
    bm = bmesh.from_edit_mesh(obj.data)

    for f in bm.faces:
        face = f.normal
    r = bmesh.ops.extrude_face_region(bm, geom=bm.faces[:])
    verts = [e for e in r['geom'] if isinstance(e, bmesh.types.BMVert)]
    TranslateDirection = face * depth  # Extrude Strength/Length
    bmesh.ops.translate(bm, vec=TranslateDirection, verts=verts)

    bmesh.update_edit_mesh(obj.data)
    bm.free()

    bpy.ops.object.editmode_toggle()
    pass


def digHoleObj(obj: bpy.types.Object, obj2: bpy.types.Object) -> None:
    # Create cut object
    cut = obj2

    # Apply boolean
    bpy.context.view_layer.objects.active = obj
    boolean = obj.modifiers.new(type="BOOLEAN", name="cut_ops")
    boolean.object = cut
    boolean.solver = "FAST"
    boolean.operation = "DIFFERENCE"
    cut.hide_set(True)
    bpy.ops.object.modifier_apply(modifier="cut_ops")
    bpy.data.objects.remove(cut)
    return


def union(obj: bpy.types.Object, obj2: bpy.types.Object) -> bpy.types.Object:
    # Create cut object
    bpy.context.view_layer.objects.active = obj
    cut = obj2
    # Apply boolean
    boolean = obj.modifiers.new(type="BOOLEAN", name="union_ops")
    boolean.object = cut
    boolean.solver = "FAST"
    boolean.operation = "UNION"
    cut.hide_set(True)
    bpy.ops.object.modifier_apply(modifier="union_ops")
    bpy.data.objects.remove(cut)
    return obj


def bevelWeight(obj: bpy.types.Object, width: float, segs: int = 6) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.context.view_layer.objects.active = obj
    bv: bpy.types.BevelModifier = obj.modifiers.new(
        type="BEVEL", name="bevel")
    bv.affect = "EDGES"
    bv.offset_type = "OFFSET"
    bv.limit_method = "WEIGHT"
    bv.width = width
    bv.segments = segs
    bpy.ops.object.modifier_apply(modifier="bevel")
    return obj


def bevelEdges(object: bpy.types.Object,
               offset: float, segments: int,
               callback: Callable[[bmesh.types.BMEdge], bool]) -> None:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(object.data)
    for e in bm.edges:
        if callback(e):
            e.select_set(True)
    bpy.ops.mesh.bevel(offset=offset,
                       offset_pct=0,
                       affect='EDGES',
                       segments=segments)
    bpy.ops.object.mode_set(mode='OBJECT')


def bevelVertices(object: bpy.types.Object,
                  offset: float, segments: int,
                  callback: Callable[[bmesh.types.BMVert], bool]) -> None:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(object.data)
    for v in bm.verts:
        if callback(v):
            v.select_set(True)
    bpy.ops.mesh.bevel(offset=offset,
                       offset_pct=0,
                       affect='VERTICES',
                       segments=segments)
    bpy.ops.object.mode_set(mode='OBJECT')


def removeFaces(obj: bpy.types.Object, callback: Callable[[bmesh.types.BMFace], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for f in bm.faces:
        if callback(f):
            bm.faces.remove(f)
    bpy.ops.object.mode_set(mode='OBJECT')


def removeEdges(obj: bpy.types.Object, callback: Callable[[bmesh.types.BMEdge], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for e in bm.edges:
        if callback(e):
            e.select_set(True)
    bpy.ops.mesh.delete(type='EDGE_FACE')
    bpy.ops.object.mode_set(mode='OBJECT')


def removeVertice(obj: bpy.types.Object, callback: Callable[[bmesh.types.BMVert], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if callback(v):
            v.select_set(True)
    bpy.ops.mesh.delete(type='VERT')
    bpy.ops.object.mode_set(mode='OBJECT')


def moveVertice(obj: bpy.types.Object, direction: Vector, callback: Callable[[bmesh.types.BMVert], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='VERT')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for v in bm.verts:
        if callback(v):
            v.select_set(True)
    bpy.ops.transform.translate(value=direction)
    bpy.ops.object.mode_set(mode='OBJECT')


def extrudeAlongNorm(obj: bpy.types.Object, depth: float, callback: Callable[[bmesh.types.BMFace], bool]) -> None:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for f in bm.faces:
        if callback(f):
            f.select_set(True)
    bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region={"use_normal_flip": False, "use_dissolve_ortho_edges": False, "mirror": False},
                                              TRANSFORM_OT_shrink_fatten={"value": depth, "use_even_offset": False, "mirror": False, "use_proportional_edit": False, "proportional_edit_falloff": 'SMOOTH',
                                              "proportional_size": 1, "use_proportional_connected": False, "use_proportional_projected": False, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "release_confirm": False, "use_accurate": False})
    bpy.ops.object.mode_set(mode='OBJECT')


def subdivideEdges(obj: bpy.types.Object, callback: Callable[[bmesh.types.BMEdge], bool], slices: int = 1) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for e in bm.edges:
        if callback(e):
            e.select_set(True)
    bpy.ops.mesh.subdivide(number_cuts=slices)
    bpy.ops.object.mode_set(mode='OBJECT')


def moveEdges(obj: bpy.types.Object | bmesh.types.BMFace, direction: Vector, callback: Callable[[bmesh.types.BMEdge], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action="DESELECT")

    if isinstance(obj, bpy.types.Object):
        bm = bmesh.from_edit_mesh(obj.data)
        for e in bm.edges:
            if callback(e):
                e.select_set(True)
    elif isinstance(obj, bmesh.types.BMFace):
        for e in obj.edges:
            if callback(e):
                e.select_set(True)

    bpy.ops.transform.translate(value=direction)

    bpy.ops.object.mode_set(mode='OBJECT')


def extrudeEdges(obj: bpy.types.Object | bmesh.types.BMFace, direction: Vector, callback: Callable[[bmesh.types.BMEdge], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='EDGE')
    bpy.ops.mesh.select_all(action="DESELECT")

    if isinstance(obj, bpy.types.Object):
        bm = bmesh.from_edit_mesh(obj.data)
        for e in bm.edges:
            if callback(e):
                e.select_set(True)
    elif isinstance(obj, bmesh.types.BMFace):
        for e in obj.edges:
            if callback(e):
                e.select_set(True)

    bpy.ops.mesh.extrude_edges_move(MESH_OT_extrude_edges_indiv={"use_normal_flip": False, "mirror": False}, TRANSFORM_OT_translate={"value": direction, "orient_axis_ortho": 'X', "orient_type": 'GLOBAL', "orient_matrix": ((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type": 'GLOBAL', "constraint_axis": (False, False, False), "mirror": False, "use_proportional_edit": False, "proportional_edit_falloff": 'SMOOTH',
                                    "proportional_size": 1, "use_proportional_connected": False, "use_proportional_projected": False, "snap": False, "snap_target": 'CLOSEST', "snap_point": (0, 0, 0), "snap_align": False, "snap_normal": (0, 0, 0), "gpencil_strokes": False, "cursor_transform": False, "texture_space": False, "remove_on_cancel": False, "view2d_edge_pan": False, "release_confirm": False, "use_accurate": False, "use_automerge_and_split": False})
    bpy.ops.object.mode_set(mode='OBJECT')


def moveFaces(obj: bpy.types.Object, direction: Vector, callback: Callable[[bmesh.types.BMFace], bool]) -> bpy.types.Object:
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_mode(type='FACE')
    bpy.ops.mesh.select_all(action="DESELECT")
    bm = bmesh.from_edit_mesh(obj.data)
    for f in bm.faces:
        if callback(f):
            f.select_set(True)
    bpy.ops.transform.translate(value=direction)
    bpy.ops.object.mode_set(mode='OBJECT')
