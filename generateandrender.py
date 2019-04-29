import bpy
#from chiplotle import *
#from svgpathtools import svg2paths, Path, Line, Arc, CubicBezier, QuadraticBezier
import random
import sys
import tracery
from tracery.modifiers import base_english

layers = [False]*20
layers[0] = True
print(sys.argv)
sysargvoffset = 5

def dosomegeom():
    for locx in range(0,15,3):
        for locy in range(0,15,5):
            print("blasah")
            add_cube(location=[locx*1,locy*1,random.random()*3])


add_cube = bpy.ops.mesh.primitive_cube_add
def multicubegeom(cubenum, union):
    #rot = [23,45,15]
    for i in range(0,int(cubenum),1):
        rot = [random.random()*90,random.random()*90,random.random()*90]
        loc = [random.random()*3, random.random()*3, random.random()*3]
        #rad = random.random()*2
        rad = random.random()*1.3
        add_cube(location=loc,rotation=rot, radius=rad)
        bpy.ops.transform.resize(value=(random.random()*40, 1.0, 1.0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', )
    if (union == 'union'):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.modifier_apply(modifier="Auto Boolean")
        bpy.ops.btool.auto_union(solver='BMESH')
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.view3d.camera_to_view_selected()

add_curve = bpy.ops.curve.primitive_bezier_curve_add
def bezierStack():
    loc = [random.random()*3, random.random()*3, random.random()*3]
    add_curve(view_align=False, location=loc)
    pass


def addtextstuff(text, scale):
    print ("plottinhG: "+ text)
    #bpy.ops.font.open(filepath="//../plotterexperiments/rus.ttf", relative_path=True)
    for idx,letter in enumerate(text):
        print(idx,letter)
        bpy.ops.object.text_add(view_align=False, enter_editmode=False, location=(idx*scale,0,0))
        bpy.ops.object.editmode_toggle()
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.delete(type='PREVIOUS_OR_SELECTION')
        bpy.ops.font.text_insert(text=letter)
        bpy.ops.object.editmode_toggle()
        bpy.context.object.data.font = bpy.data.fonts["Russian"]
        bpy.context.object.data.extrude = 0.1
        bpy.context.object.data.bevel_depth = 0.1
        bpy.ops.object.convert(target='MESH')

    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.modifier_apply(modifier="Auto Boolean")
    bpy.ops.btool.auto_union(solver='BMESH')
    #bpy.ops.mesh.remove_doubles()
    bpy.ops.transform.rotate(value=1.22173, axis=(1, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.rotate(value=-1.5708, axis=(0, 0, 1), constraint_axis=(False, False, True), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    bpy.ops.transform.translate(value=(-8.2, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)
   # bpy.context.object.data.extrude = 1
 #   v = bpy.context.object.dimensions
    
#    v[0]
    bpy.ops.view3d.camera_to_view_selected()
    bpy.ops.transform.resize(value=(0.99, 0.99, 0.99), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)


def setFreestyleContext():
    bpy.context.scene.render.layers["fressstylelayer"].use_solid = False
    bpy.context.scene.render.layers["fressstylelayer"].use_halo = False
    bpy.context.scene.render.layers["fressstylelayer"].use_zmask = False
    bpy.context.scene.render.layers["fressstylelayer"].use_all_z = False
    bpy.context.scene.render.layers["fressstylelayer"].use_ztransp = False
    bpy.context.scene.render.layers["fressstylelayer"].invert_zmask = False
    bpy.context.scene.render.layers["fressstylelayer"].use_sky = False
    bpy.context.scene.render.layers["fressstylelayer"].use_edge_enhance = False
    bpy.context.scene.render.layers["fressstylelayer"].use_strand = False
    bpy.context.scene.render.layers["fressstylelayer"].use_freestyle = True

    bpy.context.scene.render.use_freestyle = True
    #change to script mode
    rl = bpy.context.scene.render.layers.active
    rl.freestyle_settings.mode = 'EDITOR'



def setRenderParams():
    
    bpy.context.scene.render.resolution_y = 2970 
    bpy.context.scene.render.resolution_x = 4200
    bpy.context.scene.render.resolution_percentage = 50
    


def renderStuff():
    #render image
    bpy.context.scene.render.filepath = './' + sys.argv[sysargvoffset+1]
    bpy.ops.render.render( write_still=True )


rules = {
    'origin': '#hello.capitalize#, #location#!',
    'hello': ['hello', 'greetings', 'howdy', 'hey'],
    'location': ['world', 'solar system', 'galaxy', 'universe']
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)

def dostufff():
  #  print(grammar.flatten("#origin#"))  # prints, e.g., "Hello, world!"
    return(grammar.flatten("#origin#"))


#dosomegeom()
multicubegeom(sys.argv[sysargvoffset+2], sys.argv[sysargvoffset+3])
#multicubegeom(30, 'union')
#bezierStack()

# #addtextstuff("errors and mistakes",0.7)
# text = dostufff()
# addtextstuff(text,0.7)
#addtextstuff(sys.argv[sysargvoffset+4],0.7)
setFreestyleContext()
setRenderParams()
renderStuff()
#print("doing: " + sys.argv[sysargvoffset+3])
