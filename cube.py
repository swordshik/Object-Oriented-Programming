from shape_3d import Shape3D
import math

class Cube(Shape3D):
    
    def __init__(self, side_length: float):
        self.side_length = side_length
        
    def surface_area(self) -> float:
        return 6 * self.side_length ** 2
    
    def volume(self) -> float:
        return self.side_length ** 3