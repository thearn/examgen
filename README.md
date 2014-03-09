Math exam generator
====================

A Python class that can automatically generate mathematics worksheets/exams, with 
solution keys, using Sympy and LaTeX. Meant for instructors, tutors, and student
study groups, etc.

# Requirements
- Python 2.7 (Python 3 support coming soon)
- Sympy
- LaTeX

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

The are functions which
require no arguments, and return a tuple of two LaTeX-compatible strings each 
time they are called. The first string is the problem generated, the second is
the corresponding solution.

For example, this is the quadratic equation generator/solver:
```Python
def make_quadratic_eq(x="x", rhs = None):
    """
    Generates quadratic equation problem expression and
    set of solutions

    x : charector for the variable to be solved for. defaults to "x".
    
    rhs : value to set for the right-hand side. If not given, the 
          right-hand side will be a randomly generated polynomial expression
          of degree <= 2, in the same variable.
    """
    x = sympy.Symbol(x)
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
random coefficients, and `render(string)` is a function that places $$ charectors
properly for LaTeX rendering.

The `exam.add_section()` method will actually accept any function that returns 
two strings as a problem generator, in addition to a text alias. 
This way, the code can be easily extended to new subject areas.

Over time, I plan on extending built-in support for problem types from elementary
algebra and trigonometry through calculus, differential equations, and linear
algebra (and likely beyond). I'm also planning on extending support for generating
exams from static sets of problems (rather than purely generated ones). This could
be very helpful for graduate level material or qualifier exam prep.



