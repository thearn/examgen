Math exam generator
====================

A Python class that can automatically generate mathematics worksheets/exams, with 
solution keys, using Sympy and LaTeX. Meant for instructors, tutors, and student
study groups, etc.

# Requirements
- Python 2.7 (Python 3 support coming soon)
- Sympy
- LaTeX

## Installing
Dependencies available as Python packages can be installed with

`pip install -r requirements.txt`

# Quickstart Example

```Python
from examgen import exam

# make an exam with a filename and title
myexam = exam("algebra1", "Algebra 101 exam 1")

# add some problem sections
# syntax: problem type, # of problems, section title, instructions
myexam.add_section("Linear equations", 20, "Linear equations",
                   "Solve the following equations for the specified variable.")
myexam.add_section("Quadratic equations", 20, "Quadratic equations",
                   "Solve the following quadratic equations.")

# generate the exam and solutions pdf
myexam.write()
```
Running this code will generate [algebra1.pdf](algebra1.pdf) and 
[algebra1_solutions.pdf](algebra1_solutions.pdf). The LaTeX `.tex`, `.log` and
`.aux` files will automatically be deleted after compiling. If you would rather
save the `.tex` files for further modifications, pass the `savetex` flag when
making your exam:

```Python
myexam = exam("algebra1", "Algebra 101 exam 1", savetex=True)
```

The two problem types used above (`"Linear equations"` and `"Quadratic equations"`)
are aliases to linear and quadratic problem generators defined in 
[examgen/lib/algebra.py](examgen/lib/algebra.py) (`make_linear_eq` and `make_quadratic_eq`, respectively).

The are functions which may or may not require any arguments, but always return 
a tuple of two LaTeX-compatible strings each 
time they are called. The first string is the problem generated, the second is
the corresponding solution.

For example, this is the quadratic equation generator/solver:
```Python
def make_quadratic_eq(x="x", rhs = None):
    """
    Generates quadratic equation problem expression and
    set of solutions

    x : character for the variable to be solved for. defaults to "x".
                            OR
        a list of possible characters. A random selection will be made from them.
    
    rhs : value to set for the right-hand side. If not given, the 
          right-hand side will be a randomly generated polynomial expression
          of degree <= 2, in the same variable.
    """
    if isinstance(x, str):
        x = sympy.Symbol(x)
    elif isinstance(x, list):
        x = sympy.Symbol(random.choice(x))
    c1, c2, c3 = get_coefficients(3)
    lhs = c1*x**2 + c2*x + c3

    if rhs == None:
        c4, c5, c6 = get_coefficients(3, first_nonzero=False)
        rhs = c4*x**2 + c5*x + c6
    
    e = sympy.Eq(lhs, rhs)
    sols = [render(ex, x) for ex in sympy.solve(e, x)]
    if len(sols) == 0:
        return make_quadratic_eq()
    return render(e), sols
```
The `get_coefficients(n)` function is just a helper function for generating
random coefficients, and `render(string)` is a function that places $$ characters
properly for LaTeX rendering.

# Extending for new problem types

The `exam.add_section()` method will actually accept any function that returns 
two strings as a problem generator, in addition to a built-in text alias. This method
will also accept arguments to be passed to problem generating functions.
This way, the code can be easily extended to new subject areas.

So for example, if you define a custom generating function `my_problem(arg1, arg2=val)` with
required argument `arg1` and keyword argument `arg2`, you can add a section of
15 problems of this type to your exam by calling:

```Python
myexam..add_section(my_problem, 15, "Cool problems",
                 "Solve these problems", arg1_val, arg2=arg2_val)
```

You can use this to refine existing problem generating functions to meet your
needs. 
For example, if you would like to generate a 10 problem section of 
quadratic equations that are in the variables x, y, or z, we see that 
the function `make_quadratic_eq()` shown above will accept a list for its 
argument `x`. So we can call:

```Python
myexam.add_section(make_quadratic_eq, 20, "Quadratic equations",
                   "Solve the following quadratic equations.", ["x", "y", "z"])
```

and this will randomly generate the quadratic equation section with problems in the 
variables x, y, and z.

# Goals

Over time, I plan on extending built-in support for problem types from elementary
algebra and trigonometry through calculus, differential equations, and linear
algebra (and likely beyond). I'm also planning on extending support for generating
exams from static sets of problems (rather than purely generated ones). This could
be very helpful for graduate level material or qualifier exam prep.

A no-installation GUI application (build using pyinstaller) would also be helpful
for educators who don't have much experience in Python or CLI.

