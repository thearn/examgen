import os
import sympy
import random
from string import ascii_lowercase
from string import ascii_uppercase
from copy import copy

# gather up alphanumeric charectors we might want to use for variable names
alpha = [i for i in ascii_uppercase + ascii_lowercase]
# remove the ones that might be confusing in a problem
alpha.remove("l")
alpha.remove("o")
alpha.remove("O")
alpha.remove("I")
alpha.remove("i")
# gather up numerical digits we might want to use for coefficients
# nothing special about -26 to 26, other than it matches the number of chars
# above
digits = range(-26,26)
# make a list of the nums above, but with zero removed. This way we know we
# can always guarantee selection of a non-zero digit (so the degree of a
# polynomial in an equation is at least a certain value)
digits_nozero = range(-26,26)
digits_nozero.remove(0)

def get_coefficients(n, exclude=["x", "X"], first_nonzero=True, var_coeffs=False, 
                        reduce=True):
    """
    Helper function to generate "good" coefficients for problems
    """
    if var_coeffs:
        selection = copy(digits_nozero + alpha)
        for i in exclude:
            selection.remove(i)
    else:
        selection = digits_nozero
    coeffs = []
    for i in xrange(n):
        c = random.choice(selection)
        if isinstance(c, str):
            c = sympy.Symbol(c)
        if reduce and random.randint(0,1):
            c = 0
        coeffs.append(c)
    if first_nonzero and coeffs[0] == 0:
        coeffs[0] = random.choice(selection)
    return coeffs

def render(expr, lhs=""):
    """
    Puts $ at the beginning and end of a latex expression.
    lhs : if we want to render something like: $x = 3 + 5$, set the left hand 
          side here
    """
    left = "$"
    if lhs:
        left = "$%s =" % lhs
    return ''.join([left, sympy.latex(expr), "$"])

def make_quadratic_eq(x="x", rhs = None):
    """
    Generates quadratic equation problem expression and
    set of solutions

    x : charector for the variable to be solved for. defaults to "x".
                            OR
        a list of possible charectors. A random selection will be made from them.
    
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

def make_linear_eq(x="", rhs = None, var_coeffs=True):
    """
    Generates linear equation in one variable, and its solution.

    x : charector for the variable to be solved for. defaults to random selection
        from the global list `alpha`.

    rhs : value to set for the right-hand side. If not given, the 
          right-hand side will be a randomly generated linear expression

    var_coeffs : sets whether we want variables as coefficients in the problem.
                 defaults to True. Set to False if you want a problem with strictly
                 numerical coefficients.
    """
    if not x:
        x = random.choice(alpha)
    elif isinstance(x, list):
        x = random.choice(x)

    exclude = [x.upper(), x.lower()]
    x = sympy.Symbol(x)
    c1, c2, c3, c4 = get_coefficients(4, var_coeffs=var_coeffs, reduce=False, 
                                      exclude = exclude)
    lhs = c1*x + c2
    rhs = c3*x + c4
    e = sympy.Eq(lhs, rhs)
    sols = [render(ex, x) for ex in sympy.solve(e, x)]
    return "Solve for $%s$ : %s" % (x, render(e)), sols

def make_rational_simply(x="x", p=2):
    print

if __name__ == "__main__":
    print make_quadratic_eq(["x", "y", "z"])




