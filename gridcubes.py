import bpy

# Number of cubes.
count = 10

# Size of grid.
extents = 8.0

# Spacing between cubes.
padding = 0.05

# Size of each cube.
sz = (extents / count) - padding

# To convert abstract grid position within loop to real-world coordinate.
iprc = 0.0
jprc = 0.0
kprc = 0.0
countf = 1.0 / (count - 1)
diff = extents * 2

# Position of each cube.
z = 0.0
y = 0.0
x = 0.0

# Center of grid.
centerz = 0.0
centery = 0.0
centerx = 0.0

# Loop through grid z axis.
for i in range(0, count, 1):

    # Convert from index to percent in range 0 .. 1,
    # then convert from prc to real world coordinate.
    # Equivalent to map(val, lb0, ub0, lb1, ub1).
    iprc = i * countf
    z = -extents + iprc * diff

    # Loop through grid y axis.
    for j in range(0, count, 1):
        jprc = j * countf
        y = -extents + jprc * diff

        # Loop through grid x axis.
        for k in range(0, count):
            kprc = k * countf
            x = -extents + kprc * diff

            # Add grid world position to cube local position.
            bpy.ops.mesh.primitive_cube_add(location=(centerx + x, centery + y, centerz + z), radius=sz)

            # Cache the current object being worked on.
            current = bpy.context.object

            # Equivalent to Java's String.format. Placeholders
            # between curly braces will be replaced by value of k, j, i.
            current.name = 'Cube ({0}, {1}, {2})'.format(k, j, i)
            current.data.name = 'Mesh ({0}, {1}, {2})'.format(k, j, i)

            # Create a material.
            mat = bpy.data.materials.new(name='Material ({0}, {1}, {2})'.format(k, j, i))

            # Assign a diffuse color to the material.
            mat.diffuse_color = (kprc, jprc, iprc)
            current.data.materials.append(mat)

# Add a sun lamp above the grid.
bpy.ops.object.lamp_add(type='SUN', radius=1.0, location=(0.0, 0.0, extents * 0.667))

# Add an isometric camera above the grid.
# Rotate 45 degrees on the x-axis, 180 - 45 (135) degrees on the z-axis.
bpy.ops.object.camera_add(location=(extents * 1.414, extents * 1.414, extents * 2.121), rotation=(0.785398, 0.0, 2.35619))
bpy.context.object.data.type = 'ORTHO'
bpy.context.object.data.ortho_scale = extents * 7.0