
import bpy
from blender_model import BlenderModel
from utils import add_cylinder, moveOrigin, union


class PU56HKnob(BlenderModel):

    knobHeight: float = 100e-4
    knobRadius1: float = 10e-3
    knobRadius2: float = 11e-3

    def __init__(self) -> None:
        super().__init__()

    def createMaterial(self) -> bpy.types.Material:
        index = bpy.data.materials.find("PU56SpeedKnob")
        if index != -1:
            return bpy.data.materials[index]
        else:
            mat: bpy.types.Material = bpy.data.materials.new(
                name=f"PU56SpeedKnob")
            mat.use_nodes = True

            nodes = mat.node_tree.nodes
            links = mat.node_tree.links

            texCoord: bpy.types.ShaderNodeTexCoord = nodes.new(
                "ShaderNodeTexCoord")
            paintNoise: bpy.types.ShaderNodeTexNoise = nodes.new(
                "ShaderNodeTexNoise")

            links.new(texCoord.outputs["Object"],
                      paintNoise.inputs["Vector"])

            paintNoise.inputs["Scale"].default_value = 5.0
            paintNoise.inputs["Detail"].default_value = 15.0
            paintNoise.inputs["Roughness"].default_value = 1.0

            roughtRamp: bpy.types.ShaderNodeValToRGB = nodes.new(
                "ShaderNodeValToRGB")
            roughtRamp.color_ramp.elements[0].color = (0.5, 0.5, 0.5, 1)
            roughtRamp.color_ramp.elements[0].position = (0.355)
            roughtRamp.color_ramp.elements[1].color = (1, 1, 1, 1)
            roughtRamp.color_ramp.elements[1].position = (1.000)

            links.new(paintNoise.outputs["Color"], roughtRamp.inputs["Fac"])
            links.new(roughtRamp.outputs["Color"],
                      nodes[0].inputs["Roughness"])

            nodes[0].inputs["Metallic"].default_value = 0.5
            nodes[0].inputs["Specular"].default_value = 0.25
            nodes[0].inputs["Base Color"].default_value = (0, 0, 0, 1)

            return mat

    def create(self) -> bpy.types.Object:

        base: bpy.types.Object = add_cylinder(
            1e-3, self.knobRadius2*1.01, self.knobRadius2*1.01, 28)
        moveOrigin((0, 0, -5e-4))
        base.location = (0, 0, 0)

        knob: bpy.types.Object = add_cylinder(
            self.knobHeight + 5e-4, self.knobRadius1, self.knobRadius2, 7)
        moveOrigin((0, 0, -(self.knobHeight+5e-4)/2))
        knob.location = (0, 0, 5e-4)

        knob = union(knob, base)
        moveOrigin((0, 0, 0))

        knob.data.materials.append(self.createMaterial())
        return knob
