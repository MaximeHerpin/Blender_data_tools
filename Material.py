import bpy
import mathutils
from math import *
from bpy.props import *



#ob = bpy.context.active_object

def Get_nodes(ob):
	mat = ob.active_material
	NT = mat.node_tree
	nodes = [i for i in NT.nodes]
	Nodes = [(n.bl_idname,n.location,n.name,n.label) for n in NT.nodes]
	Links = [([nodes.index(l.from_node),l.from_socket.name],[nodes.index(l.to_node),l.to_socket.name]) for l in NT.links]
	return Nodes,Links

#print(Get_nodes(bpy.context.active_object))

#ob = bpy.data.objects.get('target')
def create_material(ob):
	mat = material = bpy.data.materials.new(name="test")
	mat.use_nodes = True
	mat.node_tree.nodes.remove(mat.node_tree.nodes.get('Diffuse BSDF'))
	mat.node_tree.nodes.remove(mat.node_tree.nodes.get('Material Output'))
	Nodes,Links = Get_nodes(bpy.context.active_object)
	for (type,loc,name,label) in Nodes:
		new_node = mat.node_tree.nodes.new(type)
		new_node.location = loc
		new_node.name = name
		new_node.label = label
	nodes = mat.node_tree.nodes
	nodes['Mapping'].scale = (15,15,15)
	nodes["Noise Texture"].inputs[1].default_value = 2
	nodes["Noise Texture"].inputs[2].default_value = 10
	nodes["Mix"].blend_type = 'MULTIPLY'
	nodes["Mix.002"].blend_type = 'MULTIPLY'
	nodes["Mix.002"].inputs[0].default_value = .95
	nodes["Math.001"].operation = 'MULTIPLY'
	nodes["Math.001"].inputs[1].default_value = 30
	nodes["moss height"].color_ramp.elements[0].position = .3
	nodes["moss height"].color_ramp.elements[1].position = .5
	nodes["Noise Texture.001"].inputs[1].default_value = .7
	nodes["Noise Texture.001"].inputs[2].default_value = 10
	nodes["Bright/Contrast"].inputs[2].default_value = 5
	nodes["moss color"].blend_type = 'MULTIPLY'
	nodes["moss color"].inputs[2].default_value = [0.342, 0.526, 0.353, 1.0]
	nodes["color variation"].blend_type = 'OVERLAY'
	nodes["color variation"].inputs[2].default_value = [0.610, 0.648, 0.462, 1.0]
	
	
	
	links = mat.node_tree.links
	for (f,t) in Links:
		from_node = mat.node_tree.nodes[f[0]]
		to_node = mat.node_tree.nodes[t[0]]
		links.new(from_node.outputs[f[1]],to_node.inputs[t[1]])	
	ob.active_material = mat

create_material(bpy.data.objects.get('target'))

#mat = bpy.data.materials.new('tree_mat')
#mat.use_nodes = True
#nodes = mat.node_tree.nodes
#ob.active_material = mat
