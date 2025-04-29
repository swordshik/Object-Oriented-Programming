from shape_3d import Shape3D
import math

class Cylinder(Shape3D):
    
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height
        
    def surface_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)
    
    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height