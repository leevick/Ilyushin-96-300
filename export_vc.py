import bpy
import sys
import pathlib


argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.ops.wm.open_mainfile(filepath=argv[0])

settings = bpy.context.scene.msfs_multi_exporter_settings
settings.export_keep_originals = False
settings.export_texture_dir = "../texture/"


bpy.ops.msfs.reload_lod_groups()

lod_group = bpy.context.scene.msfs_multi_exporter_lod_groups[0]
lod_group.generate_xml = True
lod_group.overwrite_guid = True
lod_group.folder_name = "../SimObjects/Airplanes/uac-aircraft-il-96/model/"
lod_group.group_name = "vc"

# print(pathlib.Path(__file__).parent.as_posix())

lod = lod_group.lods[0]
lod.keep_instances = True
lod.lod_value = 0
lod.enabled = True
lod.file_name = "vc"


bpy.ops.export_scene.multi_export_gltf()
