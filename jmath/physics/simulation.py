'''
    Graphical simulation of Mechanical Systems
'''

# - Imports

from .mechanics import PhysEnv, PhysObj, Vector, Point
from ..graphics import Canvas, Rectangle

# - Classes

class GraphEnv(PhysEnv, Canvas):
    '''
        The Graphical Environment for Physical Simulations

        Parameters
        ----------

        title
            String to call the interface
        width
            Width in pixels
        height
            Height in pixels
        pixels_per_metre
            The amount of pixels that represent one metre
        fullscreen
            Make screen take up full width
        **kwargs
            Additional tkinter style configurations

    '''

    def __init__(self, title: str, width: int = 800, height: int = 800, pixels_per_metre: float = 1, fullscreen: bool = False, **kwargs):

        super().__init__(title, width, height, fullscreen, **kwargs)

        self.pixels_per_metre = pixels_per_metre

    @property
    def pixels_per_metre(self) -> float:
        """The amount of pixels that represent one metre."""
        return self._pixels_per_metre

    @pixels_per_metre.setter
    def pixels_per_metre(self, new: float):
        """Sets the amount of pixels per metre."""
        self._pixels_per_metre = new
        # Calculate metres per pixel
        self._metres_per_pixel = 1/self.pixels_per_metre

    @property
    def metres_per_pixel(self) -> float:
        """The amount of metres for every pixel."""
        return self._metres_per_pixel

    @metres_per_pixel.setter
    def metres_per_pixel(self, new: float):
        """Sets the amount of metres per pixel."""
        self._metres_per_pixel = new
        # Calculate pixels per metre
        self._pixels_per_metre = 1/self._metres_per_pixel

    def start():
        """Begins the simulation."""
        super().start()

class GraphObj(PhysObj):
    """
        Graphical Representation of a Physical Object

        Parameters
        ----------

        env
            The graphical environment the 
    """
    pass
