import bpy
import bmesh
import sys
import os
import math
import pathlib


def generatePanelBackgroud(name: str) -> bpy.types.Material:

    index = bpy.data.materials.find(f"pannel_{name}")
    if index != -1:
        return bpy.data.materials[index]
    else:
        matFace = bpy.data.materials.new(name=f"pannel_{name}")
        matFace.use_nodes = True

        nodes = matFace.node_tree.nodes
        links = matFace.node_tree.links

        nodes[0].inputs['Roughness'].default_value = 1.0
        nodes[0].inputs['Specular'].default_value = 0.0
        nodes[0].inputs['Metallic'].default_value = 0.0
        nodeImage = nodes.new("ShaderNodeTexImage")
        nodeImage.image = bpy.data.images.load(
            f"{os.getcwd()}/texture/{name}.jpg", check_existing=False)
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

        bump = nodes.new("ShaderNodeBump")

        musgrave = nodes.new("ShaderNodeTexMusgrave")
        musgrave.inputs["Scale"].default_value = 47.3
        musgrave.inputs["Detail"].default_value = 15.0
        musgrave.inputs["Dimension"].default_value = 0.0

        links.new(bump.outputs['Normal'], nodes[0].inputs['Normal'])
        links.new(musgrave.outputs[0], bump.inputs[2])

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

        nodes[0].inputs['Roughness'].default_value = 0.21
        nodes[0].inputs['Specular'].default_value = 0.031
        nodes[0].inputs['Metallic'].default_value = 0.5
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
                                  rotation=(math.atan(1/3), 0, 0))
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

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix()+"/" + \
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

        bpy.context.active_object.name = 'cut'
        cut = bpy.context.active_object

        # Create base

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius, depth=self.depth, vertices=72)
        bpy.context.active_object.name = 'base'
        base = bpy.context.active_object

        # Apply boolean

        boolean = base.modifiers.new(type="BOOLEAN", name="cut_ops")
        boolean.object = cut
        boolean.operation = "DIFFERENCE"
        bpy.ops.object.modifier_apply(modifier="cut_ops")
        bpy.data.objects.remove(bpy.data.objects['cut'])
        base = bpy.context.active_object
        base.data.materials.append(generateClockBase())

        # Create glass

        bpy.ops.mesh.primitive_cylinder_add(
            radius=self.radius - self.thickness, depth=1e-3, vertices=72, location=(0, 0, self.depth / 2 - self.glassPosition))
        bpy.context.active_object.name = 'glass'
        glass = bpy.context.active_object
        glass.data.materials.append(generateClockGlass())

        # Create face

        bpy.ops.mesh.primitive_circle_add(
            radius=self.radius, fill_type="NGON", location=(0, 0, -self.depth/2))
        face = bpy.context.active_object
        face.data.materials.append(generateClockFace(__class__.__name__))

        bpy.ops.object.select_all(action="DESELECT")

        face.select_set(True)
        base.select_set(True)
        glass.select_set(True)

        bpy.ops.object.join()
        bpy.context.active_object.name = __class__.__name__

        self.model = bpy.context.active_object

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

        bpy.context.view_layer.objects.active = panel
        bevel: bpy.types.BevelModifier = panel.modifiers.new(
            type="BEVEL", name="bevel")
        bevel.affect = "VERTICES"
        bevel.offset_type = "OFFSET"
        bevel.width = 15e-3 * scale
        bpy.ops.object.modifier_apply(modifier="bevel")

        bevel: bpy.types.BevelModifier = panel.modifiers.new(
            type="BEVEL", name="bevel2")
        bevel.affect = "VERTICES"
        bevel.offset_type = "OFFSET"
        bevel.width = 1e-3 * scale
        bevel.segments = 3
        bpy.ops.object.modifier_apply(modifier="bevel2")

        extrudeFace(bpy.context.active_object, depth=depth)

        # Move origin

        saved_location = bpy.context.scene.cursor.location.xyz
        bpy.context.scene.cursor.location = (0.0, -10e-3, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location.xyz = saved_location
        bpy.ops.transform.translate(value=(0, 10e-3, depth/2))

        saved_location = bpy.context.scene.cursor.location.xyz
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location.xyz = saved_location

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
            generateInstrumentBackground(__class__.__name__))

        bpy.context.view_layer.objects.active = panel
        bevel: bpy.types.BevelModifier = panel.modifiers.new(
            type="BEVEL", name="bevel")
        bevel.affect = "VERTICES"
        bevel.offset_type = "OFFSET"
        bevel.width = 15e-3
        bpy.ops.object.modifier_apply(modifier="bevel")

        bevel: bpy.types.BevelModifier = panel.modifiers.new(
            type="BEVEL", name="bevel2")
        bevel.affect = "VERTICES"
        bevel.offset_type = "OFFSET"
        bevel.width = 1e-3
        bevel.segments = 3
        bpy.ops.object.modifier_apply(modifier="bevel2")

        extrudeFace(bpy.context.active_object, depth=depth)

        # Move origin

        saved_location = bpy.context.scene.cursor.location.xyz
        bpy.context.scene.cursor.location = (0.0, -10e-3, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location.xyz = saved_location
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

        bpy.ops.object.select_all(action="DESELECT")
        rmi_compass.select_set(True)
        rmi_face.select_set(True)
        glass.select_set(True)
        panel.select_set(True)
        bpy.ops.object.join()

        saved_location = bpy.context.scene.cursor.location.xyz
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location.xyz = saved_location

        return bpy.context.active_object


class CentralPanel(BlenderModel):

    def __init__(self) -> None:
        super().__init__()

    def create(self) -> bpy.types.Object:
        width = 1742
        height = 918
        scale = 2.2

        # Create cut object
        bpy.ops.mesh.primitive_plane_add()

        x, y, z = bpy.context.active_object.dimensions
        bpy.context.active_object.dimensions = width * \
            scale / 10000.0, height * scale / 10000.0, z

        bpy.context.active_object.name = 'CentralPanelBackgroud'
        panel = bpy.context.active_object
        panel.data.materials.append(generatePanelBackgroud(__class__.__name__))

        us2_x = 51.25e-3 - width * scale / 10000.0 / 2
        us2_y = height * scale / 10000.0 / 2 - 66.25e-3

        us2: US2 = US2()
        digHole(panel, us2.radius, 1, (us2_x, us2_y, 0))
        us2.create()
        us2.model.location = (us2_x, us2_y, -10e-3)

        # RMI Outline
        rmi = RMI()
        rmiOutline = rmi.createOutline()
        rmiOutline.location = (0.14188, 0.00598, 0)

        digHoleObj(panel, rmiOutline)

        rmiModel = rmi.create()
        rmiModel.location = (0.14188, 0.00598, 0)

        bpy.ops.object.select_all(action="DESELECT")
        us2.model.select_set(True)
        panel.select_set(True)
        rmiModel.select_set(True)
        bpy.ops.object.join()

        saved_location = bpy.context.scene.cursor.location.xyz
        bpy.context.scene.cursor.location = (0.0, 0.0, 0.0)
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
        bpy.context.scene.cursor.location.xyz = saved_location

        return bpy.context.active_object

    def render(self, name: str) -> None:
        # Add render camera

        bpy.ops.object.camera_add(location=(0, -0.2, 0.6),
                                  rotation=(math.atan(1/3), 0, 0))
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

        bpy.context.scene.render.filepath = pathlib.Path.cwd().as_posix() + "/" + name
        bpy.ops.render.render(write_still=True)

        pass


argv = sys.argv
argv = argv[argv.index("--")+1:]

bpy.data.meshes.remove(bpy.data.meshes[0])
bpy.data.lights.remove(bpy.data.lights[0])
bpy.data.cameras.remove(bpy.data.cameras[0])


classModel = globals()[argv[0]]


model: BlenderModel = classModel()
model.create()
bpy.ops.wm.save_mainfile(
    filepath=f"{os.getcwd()}/{argv[0]}.blend")
model.render(argv[0])
