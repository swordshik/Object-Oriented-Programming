import random
from cylinder import Cylinder
from shape_3d import Shape3D
from cube import Cube
from circle import Circle

def generate_random(shape_type: str) -> Shape3D:
    if shape_type == 'circle':
        radius = random.uniform(1, 10)
        return Circle(radius)
    elif shape_type == 'cube':
        side_length = random.uniform(1, 10)
        return Cube(side_length)
    elif shape_type == 'cylinder':
        radius = random.uniform(1, 10)
        height = random.uniform(1, 10)
        return Cylinder(radius, height)
    else:
        raise ValueError(f"Unknown shape type: {shape_type}")
    
    
for i in range(10):
    shape = generate_random(random.choice(['circle', 'cube', 'cylinder']))
    print(shape)