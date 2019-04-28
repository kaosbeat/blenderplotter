import bpy
#from chiplotle import *
#from svgpathtools import svg2paths, Path, Line, Arc, CubicBezier, QuadraticBezier
import random
import sys

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
def multicubegeom(union):
    #rot = [23,45,15]
    rot = [random.random()*90,random.random()*90,random.random()*90]
    cubenum = sys.argv[sysargvoffset+2]
    for i in range(0,int(cubenum),1):
        loc = [random.random()*3, random.random()*3, random.random()*3]
        #rad = random.random()*2
        rad = random.random()*0.2+0.3
        add_cube(location=loc,rotation=rot, radius=rad)
    if (union == 'union'):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.modifier_apply(modifier="Auto Boolean")
        bpy.ops.btool.auto_union(solver='BMESH')

add_curve = bpy.ops.curve.primitive_bezier_curve_add
def bezierStack():
    loc = [random.random()*3, random.random()*3, random.random()*3]
    add_curve(view_align=False, location=loc)
    pass


def addtextstuff(text, scale):
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
    bpy.ops.transform.translate(value=(-4.61079, 0, 0), constraint_axis=(True, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1, release_confirm=True, use_accurate=False)


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
    bpy.context.scene.render.resolution_percentage =100
    


def renderStuff():
    #render image
    bpy.context.scene.render.filepath = './' + sys.argv[sysargvoffset+1]
    bpy.ops.render.render( write_still=True )
    


#dosomegeom()
#multicubegeom(sys.argv[sysargvoffset+3])
#bezierStack()
addtextstuff("I lost Control",0.7   )
setFreestyleContext()
setRenderParams()
#renderStuff()
#print("doing: " + sys.argv[sysargvoffset+3])
