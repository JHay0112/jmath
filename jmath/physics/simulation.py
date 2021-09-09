'''
    Graphical simulation of Mechanical Systems
'''

# - Imports

from .mechanics import PhysEnv, PhysObj, Vector, Point
from ..graphics import Canvas, Shape, Rectangle
from tkinter import Canvas as TkCanvas

# - Classes

class GraphEnv(Canvas, PhysEnv):
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
        PhysEnv.__init__(self)

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

        # Construct the mainloop
        def mainloop():
            pass

        super().start(mainloop)

class GraphObj(PhysObj):
    """
        Graphical Representation of a Physical Object

        Parameters
        ----------

        env
            The graphical environment the object belongs to
        shape
            The shape of the object, note that position associated with the shape will be overriden
        position
            The position of the object
        velocity
            The initial velocity of the object
        mass
            The mass in kilograms
        charge
            The charge in coulombs
    """
    def __init__(self, env: GraphEnv, shape: Shape, position: Point, velocity: Vector, mass: float = 0, charge: float = 0):

        self.shape = shape

        super().__init__(env, position, velocity, mass, charge)

    @property
    def position(self) -> Point:
        """The position of the object."""
        return self._position

    @position.setter
    def position(self, new_position: Point):
        """Sets a new position."""
        # Set position
        self._position = new_position
        # Calculate graphical position
        self.shape.x = self.position[0] * self.env.pixels_per_metre
        self.shape.y = (self.env.height - self.position[1]) * self.env.pixels_per_metre
        # Redraw
        self.env.draw(self.shape)

    def draw(self, canvas: TkCanvas):
        """
            Draw shape onto graphical environment
            
            canvas
                The graphical environment to draw upon
        """
        self.shape.draw(canvas)
