bl_info = {
    "name": "Gridfinity Tile Generator",
    "author": "LokiBeatsthor",
    "version": (1, 0),
    "blender": (4, 3, 2),
    "location": "View3D > Sidebar > Gridfinity",
    "description": "Adds a Gridfinity base mesh with optional magnet holes",
    "category": "Add Mesh",
}

import bpy

from . import operators
from . import ui_panels
from . import properties

modules = [operators, ui_panels, properties]

def register():
    for module in modules:
        module.register()

def unregister():
    for module in reversed(modules):
        module.unregister()

if __name__ == "__main__":
    register()