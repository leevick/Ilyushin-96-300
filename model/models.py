import bpy
import bmesh
import sys
import os
import math
import pathlib
import random

dir = pathlib.Path(__file__).parent.as_posix()
if not dir in sys.path:
    sys.path.append(dir)


def generatePanelBackgroud(name: str) -> bpy.types.Material:

    index = bpy.data.materials.find(f"pannel_{hash(name)}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"pannel_{hash(name)}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 1.0
        nodes[0].inputs['Specular'].default_value = 0.0
        nodes[0].inputs['Metallic'].default_value = 0.0
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}", check_existing=False)
        links.new(nodeImage.outputs["Color"], nodes[0].inputs["Base Color"])
        return matFace


def generateInstrumentBackground(name: str) -> bpy.types.Material:
    index = bpy.data.materials.find(f"instrument_{name}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"instrument_{name}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 1.0
        nodes[0].inputs['Specular'].default_value = 0.0
        nodes[0].inputs['Metallic'].default_value = 0.0
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}.png", check_existing=False)
        links.new(nodeImage.outputs["Color"], nodes[0].inputs["Base Color"])

        # bump = nodes.new("ShaderNodeBump")

        # musgrave = nodes.new("ShaderNodeTexMusgrave")
        # musgrave.inputs["Scale"].default_value = 47.3
        # musgrave.inputs["Detail"].default_value = 15.0
        # musgrave.inputs["Dimension"].default_value = 0.0

        # links.new(bump.outputs['Normal'], nodes[0].inputs['Normal'])
        # links.new(musgrave.outputs[0], bump.inputs[2])

        return matFace


def generateColorBump(color) -> bpy.types.Material:
    index = bpy.data.materials.find(f"color_bump_{hash(color)}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"color_bump_{hash(color)}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 0.9
        nodes[0].inputs['Specular'].default_value = 0.1
        nodes[0].inputs['Metallic'].default_value = 0.8
        nodes[0].inputs['Base Color'].default_value = color

        # bump = nodes.new("ShaderNodeBump")

        # musgrave = nodes.new("ShaderNodeTexMusgrave")
        # musgrave.inputs["Scale"].default_value = 47.3
        # musgrave.inputs["Detail"].default_value = 15.0
        # musgrave.inputs["Dimension"].default_value = 0.0

        # links.new(bump.outputs['Normal'], nodes[0].inputs['Normal'])
        # links.new(musgrave.outputs[0], bump.inputs[2])

        return matFace


def generateClockFace(name: str) -> bpy.types.Material:

    index = bpy.data.materials.find(f"face_{name}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"face_{name}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 0.9
        nodes[0].inputs['Specular'].default_value = 0.1
        nodes[0].inputs['Metallic'].default_value = 0.8
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}.png", check_existing=False)
        links.new(nodeImage.outputs["Color"], nodes[0].inputs["Base Color"])
        return matFace


def generateClockBase() -> bpy.types.Material:
    index = bpy.data.materials.find("clock_base")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matBase = bpy.data.materials.new(name="clock_base")
        matBase.use_nodes = True

        nodes = matBase.node_tree.nodes
        links = matBase.node_tree.links

        nodes[0].inputs['Base Color'].default_value = (0, 0, 0, 1)
        nodes[0].inputs['Roughness'].default_value = 0.21
        nodes[0].inputs['Specular'].default_value = 0.031
        nodes[0].inputs['Metallic'].default_value = 0.5

        bump = nodes.new("ShaderNodeBump")

        musgrave = nodes.new("ShaderNodeTexMusgrave")
        musgrave.inputs["Scale"].default_value = 47.3
        musgrave.inputs["Detail"].default_value = 15.0
        musgrave.inputs["Dimension"].default_value = 0.0

        links.new(bump.outputs['Normal'], nodes[0].inputs['Normal'])
        links.new(musgrave.outputs[0], bump.inputs[2])
        return matBase


def generateClockGlass() -> bpy.types.Material:
    index = bpy.data.materials.find("clock_glass")
    if index != -1:
        return bpy.data.materials[index]
    else:
        # Create glass material
        matGlass = bpy.data.materials.new(name="clock_glass")
        matGlass.use_nodes = True
        nodes = matGlass.node_tree.nodes
        links = matGlass.node_tree.links
        nodes[0].inputs['Base Color'].default_value = (1, 1, 1, 0)
        nodes[0].inputs['Transmission'].default_value = 1
        nodes[0].inputs['Roughness'].default_value = 0.01
        return matGlass


class BlenderModel:
    def __init__(self) -> None:
        pass

    def create(self) -> bpy.types.Object:
        pass

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.1, 0.3),
                                  rotation=(math.atan(1 / 3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 200
        light.color = (1, 1, 1)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + \
            name
        bpy.ops.render.render(write_still=True)

        pass


class US2(BlenderModel):
    radius: float
    thickness: float
    depth: float
    glassPosition: float
    model: bpy.types.Object

    def __init__(self, radius=40e-3, thickness=3e-3, depth=10e-3, glassPosition=5e-3) -> None:
        super().__init__()
        self.radius = radius
        self.thickness = thickness
        self.depth = depth
        self.glassPosition = glassPosition

    def create(self) -> bpy.types.Object:

        # Create cut object
        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius - self.thickness, depth=self.depth + 2 * self.thickness, vertices=72, location=(0, 0, 0))

        cut = bpy.context.active_object

        # Create base

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius, depth=self.depth, vertices=72)
        base = bpy.context.active_object

        # Apply boolean

        boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
        boolean.object = cut
        boolean.operation = "DIFFERENCE"
        bpy.ops.object.modifier_apply(modifier="cut_ops")
        bpy.data.objects.remove(cut)
        base = bpy.context.active_object
        base.data.materials.append(generateClockBase())

        # Create glass

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius - self.thickness, depth=1e-3, vertices=72, location=(0, 0, self.depth / 2 - self.glassPosition))
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        # Create face

        bpy.ops.mesh.primitive_circle_add(
            radius=self.radius, fill_type="NGON", location=(0, 0, -self.depth / 2))
        face = bpy.context.active_object
        face.data.materials.append(generateClockFace(__class__.__name__))

        # Create Nails

        nails = [
            Nut().create(), Nut().create(), Nut().create(), Nut().create()]

        for i in range(2):
            for j in range(2):
                nails[2 * i +
                      j].location = (375e-4 if i == 1 else -375e-4, 365e-4 if j == 1 else -365e-4, self.depth / 2)
                nails[2 * i + j].rotation_euler[2] = random.uniform(0, math.pi)
                nails[2 * i + j].data.materials.append(
                    generateColorBump((0.13, 0.258, 0.296, 1)))

        face.parent = base
        glass.parent = base
        for n in nails:
            n.parent = base

        bpy.ops.object.select_all(action="DESELECT")
        base.select_set(True)

        moveOrigin((0.0, 0, self.depth / 2))

        self.model = base

        return self.model


def digHole(obj: bpy.types.Object, radius: float, height: float, location) -> None:
    # Create cut object
    bpy.ops.mesh.primitive_cylinder_add(
        radius=radius, depth=height, vertices=72, location=location)
    cut = bpy.context.active_object

    # Apply boolean
    bpy.context.view_layer.objects.active = obj
    boolean = obj.modifiers.new(type="BOOLEAN", name="cut_ops")
    boolean.object = cut
    boolean.operation = "DIFFERENCE"
    cut.hide_set(True)
    bpy.ops.object.modifier_apply(modifier="cut_ops")
    bpy.data.objects.remove(cut)
    return


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


def bevel(obj: bpy.types.Object, width: float, segments: int = 1) -> None:
    bpy.context.view_layer.objects.active = obj
    bevel: bpy.types.BevelModifier = obj.modifiers.new(
        type="BEVEL", name="bevel")
    bevel.affect = "VERTICES"
    bevel.offset_type = "OFFSET"
    bevel.width = width
    bevel.segments = segments
    bpy.ops.object.modifier_apply(modifier="bevel")


class RMI(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def createOutline(self) -> bpy.types.Object:
        scale = 1.005
        width = 800 * scale
        height = 1150 * scale
        depth = 5e-3

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        bpy.ops.object.editmode_toggle()
        x, y, z = bpy.context.active_object.dimensions
        bpy.ops.transform.resize(
            value=(width / 10000.0 / 2.0, height / 10000.0 / 2.0, z), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        panel = bpy.context.active_object

        bevel(panel, 15e-3 * scale)

        bevel(panel, 1e-3 * scale, 3)

        extrudeFace(bpy.context.active_object, depth=depth)

        # Move origin

        moveOrigin((0.0, -10e-3, 0.0))
        bpy.ops.transform.translate(value=(0, 10e-3, depth / 2))

        moveOrigin((0.0, 0.0, 0.0))

        return bpy.context.active_object

    def create(self) -> bpy.types.Object:
        width = 800
        height = 1150
        depth = 5e-3

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        bpy.ops.object.editmode_toggle()
        x, y, z = bpy.context.active_object.dimensions
        bpy.ops.transform.resize(
            value=(width / 10000.0 / 2.0, height / 10000.0 / 2.0, z), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        panel = bpy.context.active_object
        panel.data.materials.append(
            generateClockFace(__class__.__name__))

        bevel(panel, 15e-3)

        bevel(panel, 1e-3, 3)

        extrudeFace(bpy.context.active_object, depth=depth)

        # Move origin

        moveOrigin((0.0, -10e-3, 0.0))
        bpy.ops.transform.translate(value=(0, 10e-3, 0))

        # Dig hole
        panel = bpy.context.active_object
        digHole(panel, 37e-3, 1.0, (0, 0, 0))

        # Add RMI Face
        bpy.ops.mesh.primitive_circle_add(
            radius=37e-3, fill_type="NGON", vertices=72, location=(0, 0, -depth + 1e-3))
        rmi_face = bpy.context.active_object
        rmi_face.data.materials.append(generateClockFace("RMIFace"))
        extrudeFace(rmi_face, 1e-3)

        # Add RMI compass
        bpy.ops.mesh.primitive_circle_add(
            radius=30e-3, fill_type="NGON", vertices=72, location=(0, 0, -depth + 2e-3))
        rmi_compass = bpy.context.active_object
        rmi_compass.data.materials.append(generateClockFace("RMICompass"))
        extrudeFace(rmi_compass, 1e-3)

        # Add RMI glass
        bpy.ops.mesh.primitive_cylinder_add(
            radius=37e-3, depth=1e-3, vertices=72, location=(0, 0, -0.5e-3))
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        nails = []

        for i in range(2):
            for j in range(2):
                nails.append(Nut(radius=5e-3,
                                 height=2e-3,
                                 width=1.5e-3,
                                 depth=1.8e-3).create())
                nails[2 * i +
                      j].location = (355e-4 if i == 1 else -355e-4, (440e-4 + 20e-3) if j == 1 else (-640e-4 + 20e-3), 0)
                nails[2 * i + j].rotation_euler[2] = random.uniform(0, math.pi)
                nails[2 * i + j].data.materials.append(
                    generateColorBump((0.13, 0.258, 0.296, 1)))

        bpy.ops.object.select_all(action="DESELECT")
        rmi_compass.parent = panel
        rmi_face.parent = panel
        glass.parent = panel
        for n in nails:
            n.parent = panel

        panel.select_set(True)

        moveOrigin((0.0, 0.0, 0.0))

        # Animation
        rmi_compass.animation_data_create()
        rmi_compass.animation_data.action = bpy.data.actions.new(
            name="RotationAction")
        fcurve = rmi_compass.animation_data.action.fcurves.new(
            data_path="rotation_euler", index=2
        )
        k1 = fcurve.keyframe_points.insert(
            frame=0,
            value=0
        )
        k1.interpolation = "LINEAR"
        k2 = fcurve.keyframe_points.insert(
            frame=360,
            value=2 * math.pi
        )
        k2.interpolation = "LINEAR"

        return panel


class CentralPanel(BlenderModel):

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        width = 1742
        height = 918
        scale = 2.2

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        bpy.ops.object.editmode_toggle()
        x, y, z = bpy.context.active_object.dimensions
        bpy.ops.transform.resize(
            value=(width * scale / 10000.0 / 2.0, height * scale / 10000.0 / 2.0, z), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        panel = bpy.context.active_object
        panel.data.materials.append(generateClockFace("CentralPanelBackgroud"))

        extrudeFace(panel, 0.001)

        us2_x = 51.25e-3 - width * scale / 10000.0 / 2
        us2_y = height * scale / 10000.0 / 2 - 66.25e-3

        us2: US2 = US2()
        digHole(panel, us2.radius, 1, (us2_x, us2_y, 0))
        us2.create()
        us2.model.location = (us2_x, us2_y, 0)

        # RMI Outline
        rmi = RMI()
        rmiOutline = rmi.createOutline()
        rmiOutline.location = (0.14188, 0.00598, 0)

        digHoleObj(panel, rmiOutline)

        rmiModel = rmi.create()
        rmiModel.location = (0.14188, 0.00598, 0)

        # AGR
        digHole(panel, 45e-3, 1, (-0.04292, 0.02598, 0))

        agr: bpy.types.Object = AGR().create()

        agr.location = (-0.04292, 0.02598, 0)

        # VBM
        # vbm : bpy.types.Object = VBM().create()
        vbm_outline: bpy.types.Object = VBM().createOutline()
        vbm_outline.location = (
            2465e-4 - width * 1.1 / 10000, height * 1.1 / 10000 - 650e-4, 0)
        digHoleObj(panel, vbm_outline)

        vbm: bpy.types.Object = VBM().create()
        vbm.location = (
            2465e-4 - width * 1.1 / 10000, height * 1.1 / 10000 - 650e-4, 0)

        bpy.ops.object.select_all(action="DESELECT")

        us2.model.parent = panel
        rmiModel.parent = panel
        agr.parent = panel
        vbm.parent = panel

        panel.select_set(True)

        moveOrigin((0.0, 0.0, 0.0))

        return panel

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.2, 0.6),
                                  rotation=(math.atan(1 / 3), 0, 0))
        bpy.context.scene.camera = bpy.context.object

        # Add render light

        bpy.ops.object.light_add(
            location=(0, 1, 0.5), rotation=(-math.pi / 2 + math.atan(0.5), 0, 0), type="AREA")
        light = bpy.data.lights[0]
        light.energy = 100
        light.color = (1, 1, 1)

        # Set GPU render

        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"
        bpy.context.scene.cycles.device = "GPU"
        bpy.context.preferences.addons["cycles"].preferences.get_devices()

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + name
        bpy.ops.render.render(write_still=True)

        pass


def screwAroundZ(obj: bpy.types.Object) -> bpy.types.Object:

    bpy.context.view_layer.objects.active = obj
    mod: bpy.types.ScrewModifier = obj.modifiers.new(
        type="SCREW", name="screw")
    mod.steps = 72
    # bpy.ops.object.modifier_apply(modifier="screw")

    # mod.name = "screw"
    # mod.axis = 'Z'

    # screw: bpy.types.ScrewModifier = obj.modifiers.new(
    #     type="SCREW", name="screw")
    # screw.steps = 72
    # # bevel.affect = "VERTICES"
    # # bevel.offset_type = "OFFSET"
    # # bevel.width = 15e-3 * scale


def createPolyLine(coords, name: str) -> bpy.types.Object:
    curveData = bpy.data.curves.new(name, type='CURVE')
    curveData.dimensions = '2D'
    curveData.fill_mode = 'BOTH'
    polyline = curveData.splines.new('POLY')
    polyline.points.add(len(coords) - 1)

    for i, coord in enumerate(coords):
        x, y, z = coord
        polyline.points[i].co = (x, y, z, 1)

    # create Object
    # curveOB = bpy.data.objects.new('myCurve', curveData)

    # attach to scene and validate context
    view_layer = bpy.context.view_layer
    curveOB = bpy.data.objects.new(name, curveData)
    view_layer.active_layer_collection.collection.objects.link(curveOB)

    return curveOB


class AGR(BlenderModel):
    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        shieldDepth = 5e-3
        shieldInnerRadius = 31e-3
        shieldSlopeRadius = 40e-3
        shieldOuterRadius = 45e-3
        # ballGap = 5e-3
        # ballArc = 60.0

        ballRadius = 45e-3
        ballLocationZ = - shieldDepth - ballRadius + 3e-3

        coords = [(0, shieldInnerRadius, -shieldDepth),
                  (0, shieldSlopeRadius, 0),
                  (0, shieldOuterRadius, 0)
                  ]

        curveOB = createPolyLine(coords, "agr_ball")
        curveOB.select_set(True)
        screwAroundZ(curveOB)

        bpy.ops.object.convert(target="MESH")

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action='SELECT')

        bpy.ops.uv.cube_project()

        bpy.ops.object.editmode_toggle()

        shield: bpy.types.Object = bpy.context.active_object
        shield.data.materials.append(generateClockFace("AGRShield"))

        # Add container

        curveContainer = createPolyLine(
            [(0, 0, -shieldDepth - 2 * ballRadius),
             (0, shieldOuterRadius, -shieldDepth - 2 * ballRadius),
             (0, shieldOuterRadius, 0),
             ], "agr_container")
        curveContainer.select_set(True)
        screwAroundZ(curveContainer)

        bpy.ops.object.convert(target="MESH")
        container = bpy.context.active_object
        container.data.materials.append(generateClockBase())

        # Add ball

        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=ballRadius, location=(0, 0, 0), segments=32, ring_count=16)
        ball: bpy.types.Object = bpy.context.active_object
        ball.data.materials.append(generateClockFace("AGRBall"))
        bpy.ops.object.shade_smooth()

        bpy.ops.object.editmode_toggle()
        ov = bpy.context.copy()
        ov['area'] = [a for a in bpy.context.screen.areas if a.type == "VIEW_3D"][0]
        bpy.ops.transform.rotate(
            ov, value=math.pi / 2, orient_axis='X', orient_type='LOCAL')
        bpy.ops.object.editmode_toggle()

        ball_empty = bpy.data.objects.new("empty", None)
        bpy.context.view_layer.active_layer_collection.collection.objects.link(
            ball_empty)

        ball.parent = ball_empty
        ball_empty.location = (0, 0, ballLocationZ)

        # Glass
        bpy.ops.mesh.primitive_cylinder_add(
            radius=45e-3, depth=1e-3, vertices=72, location=(0, 0, 1e-3))
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        # Nails

        nails = []

        for i in range(2):
            for j in range(2):
                nails.append(Nut(radius=5e-3,
                                 height=2e-3,
                                 width=1.5e-3,
                                 depth=1.8e-3).create())
                nails[2 * i +
                      j].location = (470e-4 if i == 1 else -470e-4, 460e-4 if j == 1 else -460e-4, 0)
                nails[2 * i + j].rotation_euler[2] = random.uniform(0, math.pi)
                nails[2 * i + j].data.materials.append(
                    generateColorBump((0.13, 0.258, 0.296, 1)))

        bpy.ops.object.select_all(action="DESELECT")
        container.parent = shield
        ball_empty.parent = shield
        glass.parent = shield
        for n in nails:
            n.parent = shield

        shield.select_set(True)
        moveOrigin((0.0, 0.0, 0.0))

        # Animation
        ball.animation_data_create()
        ball.animation_data.action = bpy.data.actions.new(
            name="agr_pitch")
        fcurve = ball.animation_data.action.fcurves.new(
            data_path="rotation_euler", index=0
        )
        k1 = fcurve.keyframe_points.insert(
            frame=0,
            value=-math.pi / 4
        )
        k1.interpolation = "LINEAR"
        k2 = fcurve.keyframe_points.insert(
            frame=90,
            value=math.pi / 4
        )
        k2.interpolation = "LINEAR"

        ball_empty.animation_data_create()
        ball_empty.animation_data.action = bpy.data.actions.new(
            name="agr_roll")
        fcurve = ball_empty.animation_data.action.fcurves.new(
            data_path="rotation_euler", index=2
        )
        k1 = fcurve.keyframe_points.insert(
            frame=0,
            value=-math.pi / 4
        )
        k1.interpolation = "LINEAR"
        k2 = fcurve.keyframe_points.insert(
            frame=90,
            value=math.pi / 4
        )
        k2.interpolation = "LINEAR"

        return shield


def importSvg(name: str) -> bpy.types.Object:
    bpy.ops.import_curve.svg(
        filepath=f"{os.getcwd()}/vectors/{name}.svg")

    collection = bpy.data.collections[1]
    curve = collection.objects[0]

    bpy.data.collections[0].objects.link(curve)
    collection.objects.unlink(curve)

    bpy.data.collections.remove(collection)

    ret: bpy.types.Object

    for obj in bpy.data.objects:
        if obj.type == "CURVE":
            obj.data.materials.clear()
            mesh = bpy.data.meshes.new_from_object(obj)
            new_obj = bpy.data.objects.new(obj.name, mesh)
            new_obj.matrix_world = obj.matrix_world
            bpy.context.collection.objects.link(new_obj)
            bpy.data.objects.remove(obj)
            ret = new_obj
            break

    return ret


def moveOrigin(org):
    saved_location = bpy.context.scene.cursor.location.xyz
    bpy.context.scene.cursor.location = org
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
    bpy.context.scene.cursor.location.xyz = saved_location


class VBM(BlenderModel):

    def __init__(self) -> None:
        super().__init__()

    def createOutline(self) -> bpy.types.Object:
        outline = importSvg("VBMBase")
        outline.select_set(True)

        bpy.context.view_layer.objects.active = outline

        bevel(outline, 1e-3, 3)

        extrudeFace(bpy.context.active_object, depth=1)

        w, h, d = bpy.context.active_object.dimensions
        bpy.context.active_object.location = (-w / 2, -h / 2, 0.5)
        moveOrigin((0, 0, 0))

        bpy.ops.object.editmode_toggle()
        bpy.ops.transform.resize(
            value=(1.005, 1.005, 1), center_override=(0, 0, 0))
        bpy.ops.object.editmode_toggle()

        return bpy.context.active_object

    def create(self) -> bpy.types.Object:

        base = importSvg("VBMBase")
        base.select_set(True)

        bpy.context.view_layer.objects.active = base

        bevel(base, 1e-3 * 1.005, 3)

        extrudeFace(bpy.context.active_object, depth=1e-3)
        w, h, d = bpy.context.active_object.dimensions
        bpy.context.active_object.location = (-w / 2, -h / 2, 0)
        moveOrigin((0, 0, 0))

        base = bpy.context.active_object

        nails = [
            Nut().create(), Nut().create(), Nut().create(), Nut().create()]

        for i in range(2):
            for j in range(2):
                nails[2 * i +
                      j].location = (370e-4 if i == 1 else -370e-4, 370e-4 if j == 1 else -370e-4, 0)
                nails[2 * i + j].rotation_euler[2] = random.uniform(0, math.pi)
                nails[2 * i + j].data.materials.append(
                    generateColorBump((0.13, 0.258, 0.296, 1)))

        for n in nails:
            n.parent = base

        return base


class Nut(BlenderModel):
    def __init__(self,
                 radius: float = 3e-3,
                 height: float = 2e-3,
                 width: float = 1e-3,
                 depth: float = 1.8e-3
                 ) -> None:
        super().__init__()

        self.height = height
        self.angle: float = math.atan(radius / (radius - height))
        self.r: float = radius / math.sin(self.angle)
        self.segs: int = math.floor(self.angle / (2.0 * math.pi) * 72.0)
        self.radius: float = radius
        self.depth: float = depth
        self.width: float = width

    def create(self) -> bpy.types.Object:
        bpy.ops.mesh.primitive_uv_sphere_add(
            radius=self.r, location=(0, 0, self.height - self.r), ring_count=8, segments=16)
        nuts = bpy.context.active_object

        bpy.ops.mesh.primitive_cube_add(location=(0, 0, -1))
        cut1 = bpy.context.active_object

        digHoleObj(nuts, cut1)

        bpy.ops.mesh.primitive_cube_add(
            location=(0, 0, self.height - self.depth + 1))
        cut2 = bpy.context.active_object
        cut2.dimensions = (self.width, 2, 2)

        digHoleObj(nuts, cut2)

        nuts = bpy.context.active_object
        nuts.select_set(True)

        bpy.ops.object.convert(target="MESH")
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type='FACE')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.cube_project()
        bpy.ops.object.editmode_toggle()

        bpy.ops.object.shade_smooth()

        moveOrigin((0.0, 0.0, 0.0))

        return bpy.context.active_object


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
# model.render(argv[0])
