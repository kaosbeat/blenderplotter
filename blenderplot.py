import bpy

layers = [False]*20
layers[0] = True

add_cube = bpy.ops.mesh.primitive_cube_add
ctx = bpy.context.scene

def dosomegeom():
    for locx in range(0,15,3):
        print("blah")
        add_cube(location=[locx*3,0,0], layer = layers)

def setFreestyleContext():
    
    # bpy.context.scene.render.layers["RenderLayer"].use_solid = False
    # bpy.context.scene.render.layers["RenderLayer"].use_halo = False
    # bpy.context.scene.render.layers["RenderLayer"].use_zmask = False
    # bpy.context.scene.render.layers["RenderLayer"].use_all_z = False
    # bpy.context.scene.render.layers["RenderLayer"].use_ztransp = False
    # bpy.context.scene.render.layers["RenderLayer"].invert_zmask = False
    # bpy.context.scene.render.layers["RenderLayer"].use_sky = False
    # bpy.context.scene.render.layers["RenderLayer"].use_edge_enhance = False
    # bpy.context.scene.render.layers["RenderLayer"].use_strand = False
    bpy.context.scene.render.layers["fs_solid"].use_freestyle = True
    bpy.context.scene.render.use_freestyle = True
    #change to script mode
    rl = bpy.context.scene.render.layers.active
    rl.freestyle_settings.mode = 'SCRIPT'
    rl.freestyle_settings.crease_angle = 2.35   
    rl.freestyle_settings.linesets['solid']
    ctx.svg_export.use_svg_export
    ctx.svg_export.mode = 'Frame'
    #use_export_strokes

def setRenderParams():
    bpy.context.scene.render.resolution_y = 1500 
    bpy.context.scene.render.resolution_x = 1500
    bpy.context.scene.render.resolution_percentage =10
    ctx.render.layers["fs_solid"].use_pass_combined
    ctx.render.layers["fs_solid"].use_pass_z

def renderStuff():
    #render image
    bpy.context.scene.render.filepath = './blah'
    bpy.ops.render.render( write_still=True )

setFreestyleContext()
setRenderParams()
renderStuff()
