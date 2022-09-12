# Given sphere_radius and pi, compute the volume of a sphere and assign sphere_volume with the volume.
# Volume of sphere = (4.0 / 3.0) π r3


pi = 3.14159
sphere_volume = 0.0

sphere_radius = float(input())

sphere_volume = (4.0 / 3.0) * pi * (sphere_radius**3)
print(f'Sphere volume: {sphere_volume:.2f}')