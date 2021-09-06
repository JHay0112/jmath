"""
    Shapes for Graphics
"""

# - Classes

class Shape:
    """
        Shape parent class
    """

class Rectangle(Shape):
    """
        Rectangle

        Parameters
        ----------

        width
            The pixel width of the rectangle
        height
            The pixel height of rectangle
    """

    def __init__(self, width: int, height: int):
        
        self.width = width
        self.height = height