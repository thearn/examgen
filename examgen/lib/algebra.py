import os
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.polys.polytools import degree
import random
from helper import alpha, digits_nozero, get_coefficients, render, shuffle


def make_quadratic_eq(var="x", rhs = None, integer=[0, 1]):
    """
    Generates quadratic equation problem expression and
    set of solutions

    x : character for the variable to be solved for. defaults to "x".
                            OR
        a list of possible characters. A random selection will be made from them.
    
    rhs : value to set for the right-hand side. If not given, the 
          right-hand side will be a randomly generated polynomial expression
          of degree <= 2, in the same variable.

    integer : determines whether generated problem will have integer roots or
              not. Default is a random selection.
    """
    if isinstance(var, str):
        var = sympy.Symbol(var)
    elif isinstance(var, list):
        var = sympy.Symbol(random.choice(var))
    if isinstance(integer, list):
        integer = random.choice(integer)
    if integer:
        r1 = random.choice(digits_nozero)
        r2 = random.choice(digits_nozero)
        lhs = (var - r1) * (var - r2)
        lhs = lhs.expand()
        rhs = 0
    else:
        c1, c2, c3 = get_coefficients(3)
        lhs = c1*var**2 + c2*var + c3

    if rhs == None:
        c4, c5, c6 = get_coefficients(3, first_nonzero=False)
        rhs = c4*var**2 + c5*var + c6
    
    e = sympy.Eq(lhs, rhs)
    pvar = str(var)
    sols = ', '.join([pvar+" = " + sympy.latex(ex) for ex in sympy.solve(e, var)])
    sols = "$$" + sols + "$$"
    if len(sols) == 0:
        return make_quadratic_eq()
    return render(e), sols

def make_linear_eq(x="", rhs = None, var_coeffs=True):
    """
    Generates linear equation in one variable, and its solution.

    x : character for the variable to be solved for. defaults to random selection
        from the global list `alpha`.
                            OR
        a list of possible characters. A random selection will be made from them.

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

def make_rational_poly_simplify(var="x"):
    """
    Generates a rational expression of 4 polynomials, to be simplified.
    Example:
        ( (x**2 + 16*x + 60) / (x**2 - 36)) / 
        ( (x**2 - 2*x - 63) / (x**2 - 5*x - 36)

    x : character for the variable to be solved for. defaults to random selection
        from the global list `alpha`.
                            OR
        a list of possible characters. A random selection will be made from them.
    """
    if not var:
        var = random.choice(alpha)
    elif isinstance(var, list):
        var = random.choice(var)

    exclude = [var.upper(), var.lower()]
    x = sympy.Symbol(var)
    select = shuffle(range(-10,-1) + range(1,10))[:6]
    e1 = sympy.prod([x - i for i in shuffle(select)[:2]]).expand()
    e2 = sympy.prod([x - i for i in shuffle(select)[:2]]).expand()
    e3 = sympy.prod([x - i for i in shuffle(select)[:2]]).expand()
    e4 = sympy.prod([x - i for i in shuffle(select)[:2]]).expand()
    L = len(set([e1, e2, e3, e4]))
    e = ((e1/e2) / (e3 / e4))
    s1 = ''.join(["\\frac{", sympy.latex(e1), "}", "{", sympy.latex(e2), "}"])
    s2 = ''.join(["\\frac{", sympy.latex(e3), "}", "{", sympy.latex(e4), "}"])
    s3 = ''.join(["$$\\frac{", s1, "}", "{", s2, "}$$"])
    pieces = str(e.factor()).split("/")
    try:
        num, denom= [parse_expr(i).expand() for i in pieces]
    except:
        return make_rational_poly_simplify(var)
    if len(pieces) !=2 or L < 4 or degree(num) > 2 or  degree(denom) > 2:
        return make_rational_poly_simplify(var)
    return s3, render(num / denom)


if __name__ == "__main__":
    print make_quadratic_eq(["x", "y"])




