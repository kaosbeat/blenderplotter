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

#for face in bm.faces:
#    face.select = False
bpy.ops.mesh.select_all(action="DESELECT")

bm.faces.ensure_lookup_table()
bm.faces[4].select = True  # select index 4

# Show the updates in the viewport
bmesh.update_edit_mesh(me, True)
#Duplicate Vert
# inset

# extrude

# repeat


