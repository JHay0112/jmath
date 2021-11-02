'''
    Graphical Interfaces
'''

# - Imports

import tkinter as tk
from .shapes import Shape
from ..linearalgebra import Point
from typing import Callable, Any

# - Classes

class Window:
    '''
        Root level graphical interface.

        Parameters
        ----------

        title
            String to call the interface
        width
            Width in pixels
        height
            Height in pixels
        fullscreen
            Make screen take up full width
        **kwargs
            Additional tkinter style configurations
    '''

    def __init__(self, title: str, width: int = 800, height: int = 800, fullscreen: bool = False):

        # Initialise
        self._title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.root = tk.Tk()

        # Reconfigure width and height if fullscreen
        if self.fullscreen:
            self.width = self.root.winfo_width()
            self.height = self.root.winfo_height()
        
        # Configure
        self.root.title(self.title)
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.attributes("-fullscreen", self.fullscreen)
        self.root.configure(background = "white")

    @property
    def title(self):
        """Title of the GUI"""
        return self._title

    @title.setter
    def title(self, new_title: str):
        """Sets a new value of the title"""
        self._title = new_title
        self.root.title(self.title)
        
    def start(self, func: Callable[[Any], Any], delay: int = 100, *args):
        """
            Start mainloop

            Parameters
            ----------
        
            func
                The function to be run as apart of the mainloop.
                Additional arguments are passed to the function.
                Anything returned by the function will be passed back to it in the next loop.
            delay
                The delay between calls to the mainloop function in milliseconds.
            args
                Arguments to be passed to the loop.
        """

        # Building mainloop
        def loop(*args):
            # Call main function
            args = func(*args)
            self.run(loop, delay, *args)

        loop(*args)
        self.root.mainloop()

    def end(self):
        """Ends the GUI mainloop"""
        self.root.destroy()

    def run(self, func: Callable, delay: int = 0, *args):
        """
            Runs a function in context of GUI.

            Parameters
            ----------

            func
                The function to be executed
            delay
                Time delay in milliseconds
            args
                Arguments to be passed to the function
        """

        self.root.after(delay, lambda: func(*args))

    def centre(self) -> Point:
        """Computes the central point of the screen"""
        return Point(self.width/2, self.height/2)

class Canvas(Window):
    '''
        Permutation of Window for drawing shapes on.

        Parameters
        ----------

        title
            String to call the interface
        width
            Width in pixels
        height
            Height in pixels
        fullscreen
            Make screen take up full width
        kwargs
            Additional tkinter style configurations
    '''

    def __init__(self, title: str, width: int = 800, height: int = 800, fullscreen: bool = False, **kwargs):
        
        # Initialise GUI
        super().__init__(title, width, height, fullscreen)

        # Add canvas
        self.canvas = tk.Canvas(self.root, height = self.height, width = self.width, background = "white", **kwargs)
        self.canvas.pack(fill = tk.BOTH)

    def draw(self, shape: Shape):
        """
            Draws a shape

            Parameters
            ----------

            shape
                Shape object to draw
        """
        shape.draw(self.canvas)