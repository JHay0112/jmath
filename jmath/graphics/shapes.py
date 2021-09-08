"""
    Shapes for Graphics
"""

# - Imports

from tkinter import Canvas

# - Classes

class Shape:
    """
        Shape parent class

        x
            Position on the x-axis
        y
            Position on the y-axis
        **kwargs
            Additional tkinter configuration
    """
    def __init__(self, x: int, y: int, **kwargs):

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
        pass

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
        **kwargs
            Additional tkinter configuration for canvas.create_rectangle
    """

    def __init__(self, width: int, height: int, x: int, y: int, **kwargs):
        
        self.width = width
        self.height = height

        super().__init__(x, y, **kwargs)

    def draw(self, canvas: Canvas):

        if self.canvas_obj != None:
            canvas.delete(self.canvas_obj)

        self.canvas_obj = canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y - self.height, **self.kwargs)