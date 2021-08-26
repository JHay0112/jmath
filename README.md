# jmath

jmath is a hobby project developing a set of mathematical tools in the Python Language.

***
## Installation
Open a terminal/command prompt and use `pip install jmath`.

***

## Documentation

Documentation can be found at https://jordanhay.com/jmath

***
## Components

### Uncertainties (jmath.uncertainties)
Provides the Uncertainty object for doing calculations upon values with associated uncertainties.
The jmath.Uncertainty object is provided by default in the top-level package.

### Linear Algebra (jmath.linearalgebra)
Provides Vector, Point, and Line objects to do linearalgebra with. These are also used as building blocks for other submodules.
The jmath.Vector, jmath.Point, and jmath.Vector objects are provided by default in the top-level package.

### Modular (jmath.modular)
Simple tools for use in modular arithmetic. 
jmath.modular_inverse and jmath.extended_gcd are provided by default in the top-level package.

### Physics (jmath.physics)
Rudimentary classification of physical objects (jmath.physics.mechanics), circuits (jmath.physics.circuits), and SI prefixes (jmath.physics.prefixes).

### Approximation (jmath.approximation)
Euler (jmath.approximation.euler_method) and Newton Method (jmath.approximation.newton_method) for approximation of Differential equations and Roots (respectively).

### Abstract (jmath.abstract)
Provides implementations of abstract data types, including linked lists, stacks, and queues.

### Cryptography (jmath.cryptography)
Provides tools for rudimentary cryptography. Currently provides Affine cipher (jmath.cryptography.affine) as well as character frequency analysis (jmath.cryptography.tools).

### Discrete (jmath.discrete)
Node, Graph, and Loop objects for use in Graph based maths.

*** 
## Testing

Open a terminal in the root director and run `pytest tests/`, this requires pytest. Tests are automatically run in Github by a Github Action.

***

## Github Workflows

Github workflows help automate testing, updating the requirements, and publishing this repo.
