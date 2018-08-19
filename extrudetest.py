import bpy
import bmesh

layers = [False]*20
layers[0] = True
# create cube
bpy.ops.mesh.primitive_cube_add(location=[0,0,0], layers = layers, enter_editmode=True)

#go into edit mode



# select random face
obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)
print(len(bm.faces))
# inset

# extrude

# repeat


