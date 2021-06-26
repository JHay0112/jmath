# jmath
jmath is a hobby project developing a set of mathematical tools in the Python Language.

***
## Installation
Open a terminal in the root directory and run `python setup.py bdist_wheel`, this should create a 'dist' folder with a '.whl' file in it. Complete installation by running `pip install dist/jmath-VERSION-py3-none-any.whl`.

***

## Testing

Open a terminal in the root director and run `pytest tests/`, this requires pytest. Tests are automatically run in Github by a Github Action.

***
## Core Components

### Uncertainties
Calculations with uncertain values.

### Linear Algebra
Currently does rudimentary vector maths. I plan to expand this to do more vector maths as well as maths with planes.

### Discrete
Node, Graph, and Loop objects for use in Graph based maths

## Additional Components

### Physics (jmath.physics)
Rudimentary classification of physical objects (jmath.physics.mechanics) and circuits (jmath.physics.circuits).
