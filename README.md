# jmath
jmath is a hobby project developing a set of mathematical tools in the Python Language.

***
## Installation
Open a terminal/command prompt and use `pip install jmath`.

***

## Documentation

Documentation can be found at [https://jordanhay.com/jmath]

***
## Components

### Uncertainties
Calculations with uncertain values.

### Linear Algebra
Vector and Line mathematics with rudimentary planes introduced.

### Discrete
Node, Graph, and Loop objects for use in Graph based maths.

### Physics (jmath.physics)
Rudimentary classification of physical objects (jmath.physics.mechanics), circuits (jmath.physics.circuits), and SI prefixes (jmath.physics.prefixes).

### Approximation (jmath.approximation)
Euler (jmath.approximation.euler_method) and Newton Method (jmath.approximation.newton_method) for approximation of Differential equations and Roots (respectively).

*** 
## Testing

Open a terminal in the root director and run `pytest tests/`, this requires pytest. Tests are automatically run in Github by a Github Action.

***

## Github Workflows

Github workflows help automate testing, updating the requirements, and publishing this repo.