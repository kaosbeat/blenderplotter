from chiplotle import *
from chiplotle.tools.geometrytools.get_bounding_rectangle import get_bounding_rectangle
from chiplotle.tools.geometrytools.get_minmax_coordinates import get_minmax_coordinates
from xml.dom import minidom
# import xpath

from svgpathtools import svg2paths, svg2paths2, Path, Line, Arc, CubicBezier, QuadraticBezier
import sys

plotunit = 0.025
virtualplotting = True
if (virtualplotting == True):
        plotter = instantiate_virtual_plotter(type="DXY1300")
else:
        plotter = instantiate_plotters( )[0]

def getGroup(svg, groupname):
	# doc = minidom.parse(svg)  # parseString also exists
	# group = doc.getElementsByID(groupname)
	# doc.unlink()

	# group = xpath.find("//*['id="+groupname+"]",l)
	# return group

#import minidom
# from xml.dom.minidom import parse as p
#parse your XML-document
	doc = minidom.parse(svg)
	print doc.childNodes[0].childNodes[1].getAttribute("id")
	# print doc.getElementById('#fressstylelayer_LineSet')  #>> None
	print doc.childNodes[0].childNodes[1].nodeValue
	# print doc.childNodes[1].childNodes[1].getAttribute("id")
	#Get all child nodes of your root-element or any element surrounding your "target" (in my example "cmmn:casePlanModel")
	nodelist = doc.getElementsByTagName("g")[0].childNodes
	print nodelist
	# i=0
	# for i in range(len(nodelist)):
	# 	if nodelist[i].getAttribute("id") == groupname:
	# 		print ("found it!")
 # 			print nodelist[i]	
	return doc.childNodes[0].childNodes[1]
# #Now find the element via the id-tag
# def find_element(id):
#  #(or whatever you want to do)

#Call find_element with the id you are looking for
# find_element(id)

def calculatesvggroup(svg):
	print ("PLOTTING stuff")
	# plotter.select_pen(pen)
	g = shapes.group([])
	# paths, attributes, svg_attributes = svg2paths2(svg)
	# print svg_attributes
	paths, attributes = svg2paths(svg)
	# print attributes
	print dir(paths[0][0].start.real)
	for path in paths:
		for segment in path:
			if isinstance(segment, Line):
				g.append(shapes.line((segment.start.real,segment.start.imag),(segment.end.real,segment.end.imag)))
			if isinstance(segment, CubicBezier):
				print "Line found"
				g.append(shapes.bezier_path([(segment.start.real,segment.start.imag),(segment.control1.real,segment.control1.imag),(segment.control2.real,segment.control2.imag),(segment.end.real,segment.end.imag)],0))
	bb = get_bounding_rectangle(g)
	bb = get_minmax_coordinates(bb.points)
	print (bb)
	print (svg + " is " + str(g.width*plotunit) + "mm")
	print (svg + " is " + str(g.height*plotunit) + "mm")
	# plotter.write(g)
	transforms.offset(g, (-bb[0][0], -bb[0][1] ))
	io.view(g)
	return({'group': g, 'bounds': bb})


def grabSVGandplotWithChiplotle(file):
    # shape = calculatesvggroup(getGroup(file.encode('utf-8'), 'fressstylelayer_LineSet'))
    shape = calculatesvggroup(file.encode('utf-8'))
    print (shape)
    plotter.write(shape)



print (sys.argv[1])
grabSVGandplotWithChiplotle(sys.argv[1])
# io.view(plotter)
