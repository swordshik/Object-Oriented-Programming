from abc import ABC, abstractmethod


class Shape3D(ABC):

    @abstractmethod
    def surface_area(self) -> float:
        pass
    
    @abstractmethod
    def volume(self) -> float:
        pass
    
    def __str__(self) -> str:
        return (f"{self.__class__.__name__}: "
                f"Surface Area = {self.surface_area():.2f}, "
                f"Volume = {self.volume():.2f}")