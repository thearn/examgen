Math exam generator
====================

A Python class that can automatically generate mathematics exams, with 
solution keys, using Sympy and LaTeX.

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
myexam.add_section("Linear equations", 20, "Linear equations",
                   "Solve the following equations for the specified variable.")
myexam.add_section(make_quadratic_eq, 20, "Quadratic equations",
                   "Solve the following quadratic equations.")

# generate the exam and solutions pdf
myexam.write()
```
Running this code will generate [algebra1.pdf](algebra1.pdf) and 
[algebra1_solutions.pdf](algebra1_solutions.pdf)
