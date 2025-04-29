from shape_3d import Shape3D
import math

class Circle(Shape3D):
    
    def __init__(self, radius: float):
        self.radius = radius
        
    def surface_area(self) -> float:
        return math.pi * self.radius ** 2
    
    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3
    
    