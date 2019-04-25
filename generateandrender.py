import bpy
#from chiplotle import *
#from svgpathtools import svg2paths, Path, Line, Arc, CubicBezier, QuadraticBezier
import random
import sys

layers = [False]*20
layers[0] = True
print(sys.argv)
add_cube = bpy.ops.mesh.primitive_cube_add
sysargvoffset = 5

def dosomegeom():
    for locx in range(0,15,3):
        for locy in range(0,15,5):
            print("blasah")
            add_cube(location=[locx*1,locy*1,random.random()*3])

def multicubegeom(union):
    #rot = [23,45,15]
    rot = [random.random()*90,random.random()*90,random.random()*90]
    cubenum = sys.argv[sysargvoffset+2]
    for i in range(0,int(cubenum),1):
        loc = [random.random()*3, random.random()*3, random.random()*3]
        rad = random.random()*2
        #rad = random.random()*0.2+0.3
        add_cube(location=loc,rotation=rot, radius=rad)
    if (union == 'union'):
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.modifier_apply(modifier="Auto Boolean")
        bpy.ops.btool.auto_union(solver='BMESH')


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
    
    bpy.context.scene.render.resolution_y = 1500 
    bpy.context.scene.render.resolution_x = 1500
    bpy.context.scene.render.resolution_percentage =100
    


def renderStuff():
    #render image
    bpy.context.scene.render.filepath = './' + sys.argv[sysargvoffset+1]
    bpy.ops.render.render( write_still=True )
    
def calculatesvggroup(svg):
	print ("PLOTTING stuff")
	# plotter.select_pen(pen)
	g = shapes.group([])
	paths, attributes = svg2paths(svg)
	# print dir(paths[0][0].start.real)
	for path in paths:
		for segment in path:
			if isinstance(segment, Line):
				# print "Line found"
				g.append(shapes.line((segment.start.real,segment.start.imag),(segment.end.real,segment.end.imag)))
			if isinstance(segment, CubicBezier):
				g.append(shapes.bezier_path([(segment.start.real,segment.start.imag),(segment.control1.real,segment.control1.imag),(segment.control2.real,segment.control2.imag),(segment.end.real,segment.end.imag)],0))
	bb = get_bounding_rectangle(g)
	bb = get_minmax_coordinates(bb.points)
	print (bb)
	print (svg + " is " + str(g.width*plotunit) + "mm")
	print (svg + " is " + str(g.height*plotunit) + "mm")
	# plotter.write(g)
	transforms.offset(g, (-bb[0][0], -bb[0][1] ))
	io.view(g)
#    return {'group': g, 'bounds': bb}

def initPlotter():
    virtualplotting = True
    if (virtualplotting == True):
        plotter = instantiate_virtual_plotter(type="DXY1300")
    else:
        plotter = instantiate_plotters( )[0]



def grabSVGandplotWithChiplotle():
    file = "blah0001.svg"
    shape = calculatesvggroup(file.encode('utf-8'))
    plotter.write(shape)


#dosomegeom()
multicubegeom(sys.argv[sysargvoffset+3])
setFreestyleContext()
setRenderParams()
renderStuff()
print("doing: " + sys.argv[sysargvoffset+3])
#initPlotter()
#grabSVGandplotWithChiplotle()
