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

def shuffle(x):
    x = list(x)
    random.shuffle(x)
    return x

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
    left = "$$"
    if lhs:
        left = "$$%s =" % lhs
    return ''.join([left, sympy.latex(expr), "$$"])




