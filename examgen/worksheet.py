import os
from lib import doc_parts, section_parts
from lib import make_quadratic_eq, make_linear_eq, make_rational_poly_simplify
from lib import make_poly_ratio_limit, make_chain_rule_prob

_problems_map = {"Quadratic equations" : make_quadratic_eq,
                 "Linear equations" : make_linear_eq,
                 "Simplify quadratic ratio" : make_rational_poly_simplify,
                 "Limit of polynomial ratio" : make_poly_ratio_limit}


class document(object):
    """
    Small class for managing the documents and compiling them
    """
    def __init__(self, fname, title="", savetex=False, doc_generator = doc_parts):
        self.savetex = savetex
        self.start, self.end = doc_generator(title)
        self.main = []
        self.fname = fname

    def add(self, code):
        """
        Adds new sections to the document
        """
        self.main.append(code)

    def write_compile(self, remove_aux=True):
        """
        Writes and compiles into a pdf
        """
        main = '\n'.join(self.main)
        doc = '\n'.join([self.start, main, self.end])
        f = open("%s.tex" % self.fname, "wb")
        f.write(doc)
        f.close()
        os.system("pdflatex %s.tex" % self.fname)
        os.remove("%s.log" % self.fname)
        if remove_aux:
            os.remove("%s.aux" % self.fname)
        if not self.savetex:
            os.remove("%s.tex" % self.fname)




class worksheet(object):
    """
    Class for managing an worksheet.
    """
    def __init__(self, fname, title="", savetex=False):
        """
        fname : file name for the worksheet
        title : title to be placed in the worksheet
        savetex : flag to either save or delete the .tex files after compiling
        """

        self.fname = fname
        self.worksheet = document(fname, title, savetex)
        self.solutions = document(fname + "_solutions", title + " Solutions",
                                  savetex)

    def add_section(self, problem_type, n, title, instructions, cols=2,
                    *args, **kwargs):
        """
        Method for adding a section of problems to an worksheet & solutions.
        problem_type : name of the type of problem, which is mapped to a
                       problem generating function shown at the top of this file

                                                OR
                       
                       A problem generating function directly. This function
                       must take no arguments, and return a tuple of two strings.
                       The first string gives the problem, the second string it's
                       solution.
        n : the number of problems to generate for this section.
        title : title text for the section
        instructions : text instructions for the section
        """
        if hasattr(problem_type, '__call__'):
            prob_generator = problem_type
        else:
            prob_generator = _problems_map[problem_type]

        start, end = section_parts(title, instructions, cols)
        sol_start, sol_end = section_parts(title, "", cols=1)
        s_probs, s_sols = [], []
        for i in xrange(n):
            p, sols = prob_generator(*args, **kwargs)
            if not isinstance(sols, list):
                sols = [sols]
            prob = "\item " + p
            sols = "\item" + ', '.join(sols)
            s_sols.append(sols)
            s_probs.append(prob)

        s_probs = '\n'.join(s_probs)
        s_sols = '\n'.join(s_sols)
        prob_code = ''.join([start, s_probs, end])

        sol_code = ''.join([sol_start, s_sols, sol_end])
        
        self.worksheet.add(prob_code)
        self.solutions.add(sol_code)

    def write(self):
        self.worksheet.write_compile()
        self.solutions.write_compile()


if __name__ == "__main__":

    myworksheet = worksheet("algebra1", "Algebra 101 worksheet 1", savetex=True)
    myworksheet.add_section("Linear equations", 10, "Linear equations",
                       "Solve the following equations for the specified variable.")
    myworksheet.add_section("Simplify quadratic ratio", 10, "Simplify each expression",
                       "")
    myworksheet.add_section(make_quadratic_eq, 10, "Quadratic equations",
                       "Solve the following quadratic equations.", ["x", "y", "z"])
    myworksheet.add_section("Limit of polynomial ratio", 10, "Determine each limit",
                       "")
    myworksheet.add_section(make_chain_rule_prob, 10, "Evaluate",
                       "")
    myworksheet.write()



