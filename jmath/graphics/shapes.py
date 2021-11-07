"""
    Shapes for Graphics
"""

# - Imports

from tkinter import Canvas

# - Classes

class Shape:
    """
        Shape parent class

        Parameters
        ----------

        x
            Position on the x-axis
        y
            Position on the y-axis
        kwargs
            Additional tkinter configuration
    """
    def __init__(self, x: int = 0, y: int = 0, **kwargs):

        self.x = x
        self.y = y
        self.kwargs = kwargs
        self.canvas_obj = None

    def draw(self, canvas: Canvas):
        """
            Draws the object onto a canvas.
            
            Parameters
            ----------
        
            canvas
                The tkinter canvas to be drawn on
                
            Notes
            -----
            
            This method is intended to be used by the jmath.graphics.Canvas.draw() method, not accessed directly.
        """
        return NotImplemented

    def scale(self, factor: float):
        """
            Scales the object by a given factor

            Parameters
            ----------

            factor
                The factor to scale the object by
        """
        return NotImplemented

class Rectangle(Shape):
    """
        Rectangle

        Parameters
        ----------

        width
            The pixel width of the rectangle
        height
            The pixel height of rectangle
        x
            Position on the x-axis
        y
            Position on the y-axis
        kwargs
            Additional tkinter configuration for canvas.create_rectangle
    """

    def __init__(self, width: int, height: int, x: int = 0, y: int = 0, **kwargs):
        
        self.width = width
        self.height = height

        super().__init__(x, y, **kwargs)

    def draw(self, canvas: Canvas):

        if self.canvas_obj != None:
            canvas.delete(self.canvas_obj)

        self.canvas_obj = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y - self.height, **self.kwargs)

    def scale(self, factor: float):

        self.width *= factor
        self.height *= factor

class Circle(Shape):
    """
        Circle

        Parameters
        ----------

        radius
            The pixel width of the rectangle
        x
            Position on the x-axis
        y
            Position on the y-axis
        kwargs
            Additional tkinter configuration for canvas.create_rectangle
    """

    def __init__(self, radius: float, x: int = 0, y: int = 0, **kwargs):
        
        self.radius = radius

        super().__init__(x, y, **kwargs)

    def draw(self, canvas: Canvas):

        if self.canvas_obj != None:
            canvas.delete(self.canvas_obj)

        self.canvas_obj = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, **self.kwargs)

    def scale(self, factor: float):

        self.radius *= factor