import bpy
import bmesh
from mathutils import Vector, Matrix
from random import random, randint
from math import pi, radians, exp
import os.path

def roundtuple(t):
	x,y = t
	return (round(x,2),round(y,2))

path = "C:/Users/Maxime/Documents/max/3D/blender/addons/tree/modular tree"

def store_uv():
    me = bpy.context.object.data
    bm = bmesh.new()   # create an empty BMesh
    bm.from_mesh(me)
    uv_list = [[] for i in bm.faces]
    uv_layer = bm.loops.layers.uv.active
    for face in bm.faces:
        for loop in face.loops:
            uv_list[face.index].append(roundtuple(loop[uv_layer].uv))
    name = os.path.join(path, "uv.txt")
    file1 = open(name, "w")
    file1.write(str(uv_list))
    print(uv_list)
    bm.free()

store_uv()
