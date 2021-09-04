'''
    Graphical Interfaces
'''

# - Imports

import tkinter as tk
from functools import wraps
from typing import Callable

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
    '''

    def __init__(self, title: str, width: int = 800, height: int = 800, fullscreen: bool = False):

        # Initialise
        self._title = title
        self.width = width
        self.height = height
        self.fullscreen = fullscreen
        self.root = tk.Tk()

        # Reconfigure width and height if fullscreen
        if fullscreen:
            self.width = self.root.winfo_width()
            self.height = self.root.winfo_height()
        
        # Configure
        self.root.title(self.title)
        self.root.geometry(f"{width}x{height}")
        self.root.attributes("-fullscreen", self.fullscreen)
        
        self.root.mainloop()

    @property
    def title(self):
        """Title of the GUI"""
        return self._title

    @title.setter
    def title(self, new_title: str):
        """Sets a new value of the title"""
        self._title = new_title
        self.root.title(self.title)

    def run(self, func: Callable, ms: float = 0, **kwargs):
        """
            Runs a function after a given amount of time.
            Implemented through root.after.

            Parameters
            ----------

            func
                The function to run.
            ms
                Number of milliseconds to run it after.
            **kwargs
                Keyword arguments to be passed to the function.
        """
        self.root.after(ms, lambda: func(**kwargs))

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
    '''

    def __init__(self, title: str, width: int = 800, height: int = 800, fullscreen: bool = False):
        
        # Initialise GUI
        self.super().__init__(title, width, height, fullscreen)

        # Add canvas
        self.canvas = tk.Canvas()
        self.canvas.pack(expand = True)
