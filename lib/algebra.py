import os
import sympy
import random
from string import ascii_lowercase
from string import ascii_uppercase
from copy import copy

alpha = [i for i in ascii_uppercase + ascii_lowercase]
alpha.remove("l")
alpha.remove("o")
alpha.remove("O")
alpha.remove("I")
alpha.remove("i")
digits = range(-26,26)
digits_nozero = range(-26,26)
digits_nozero.remove(0)

def get_coefficients(n, exclude=["x", "X"], first_nonzero=True, var_coeffs=False, 
                        reduce=True):
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
    left = "$"
    if lhs:
        left = "$%s =" % lhs
    return ''.join([left, sympy.latex(expr), "$"])

def make_quadratic_eq(x="x", rhs = None):
    """
    Generates quadratic equation problem expression and
    set of solutions
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

def make_linear_eq(x="", rhs = None, var_coeffs=True):
    """
    Generates linear equation in one variable, and its solution
    """
    if not x:
        x = random.choice(alpha)
    exclude = [x.upper(), x.lower()]
    x = sympy.Symbol(x)
    c1, c2, c3, c4 = get_coefficients(4, var_coeffs=var_coeffs, reduce=False, 
                                      exclude = exclude)
    lhs = c1*x + c2
    rhs = c3*x + c4
    e = sympy.Eq(lhs, rhs)
    sols = [render(ex, x) for ex in sympy.solve(e, x)]
    return "Solve for $%s$ : %s" % (x, render(e)), sols

if __name__ == "__main__":
    print make_linear_eq("a")




