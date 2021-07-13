'''
    jmath/quickplot.py

    Author: Jordan Hay
    Date: 2021-07-13

    Wrapper around matplotlib for quickly plotting equations
'''

# - Imports

from matplotlib import pyplot as plt
from numpy import linspace

# - Functions

def equation(eq, title = "", x_label = "x", y_label = "y", samples = 500, x_limits = (-10, 10), y_limits = (None, None)):
    """Plots an algebraic equation (any included functions must be compatible with numpy arrays)
    
        eq (func) - The function equation to plot, should have one parameter as input and must be written with numpy functions if any
        title (str:"") - Title of equation
        x_label (str:"x") - X Label
        y_label (str:"y") - Y Label
        samples (int:500) - Amount of equation samples to take
        x_limits (int:-10, int:10) - Lower and upper bounds respectively of x
        y_limits (y_low:None, y_high:None) - Lower and upper bounds respectively of y
    """

    # Sample equation
    x_vals = linspace(x_limits[0], x_limits[1], samples)
    y_vals = eq(x_vals)

    # Setup axes
    axes = plt.axes()

    # Setup plot
    axes.set_title(title)
    axes.set_xlabel(x_label)
    axes.set_ylabel(y_label)
    plt.grid(True)
    axes.plot(x_vals, y_vals)

    # Display it
    plt.show()
