from typing import Iterable, List


def doc_parts(title="", author=""):
    start=r"""
    \documentclass{article}
    \usepackage{amsfonts}
    \usepackage{amsmath,multicol,eso-pic}
    \begin{document}
    """

    intro="""\\title{%s}
    
    \\date{\\vspace{-5ex}}  
    
    \\maketitle""" % title

    if title:
        start = start + intro

    end=r"""
    \end{document}
    """
    return start, end

def exam_parts(title="", author=""):
    start=r"""
    \documentclass{exam}
    \usepackage{amsfonts}
    \usepackage{amsmath,multicol,eso-pic}
    \noprintanswers
    \addpoints 
    \qformat{\textbf{Question \\ \thequestion}\quad(\thepoints)\hfill}
    \usepackage{color}
    \definecolor{SolutionColor}{rgb}{0.8,0.9,1} 
    \shadedsolutions 
    \renewcommand{\solutiontitle}{\noindent\textbf{Solution:}\par\noindent}

    \begin{document}
    \AddToShipoutPicture{
        \AtTextUpperLeft{
        \makebox(400,45)[lt]{ 
          \footnotesize
          \begin{tabular}{r@{\,}l}
            Name:  & \rule{0.5\linewidth}{\linethickness} \\[.5cm]
            Date:  & \rule{0.5\linewidth}{\linethickness} \\
          \end{tabular}
    }}}
    \begin{minipage}{.8\textwidth}
    This exam includes \numquestions\ questions. The total number of points is \numpoints.
    \end{minipage}
    \begin{questions}
    """

    end = r"""\end{questions}
    \end{document}
    """
    return start, end

def section_parts(title, instr="", cols = 2):

    if isinstance(cols, List):
        cols=len(cols)
    if cols >= 2:
        section_start=r"""
        \section{%s}
        %s
        \begin{multicols}{1}
        \begin{enumerate}
        """ % (title, instr)

        section_end=r"""
        \end{enumerate}
        \end{multicols}
        """
    else:
        section_start = r"""
        \section{%s}
        %s
        \begin{enumerate}
        """ % (title, instr)
        section_end = r"""
        \end{enumerate}
        """
    return section_start, section_end


def problem(instructions, problem, solution, points=1):
    code = r"""
    \question[%s]
        %s
        %s
    \begin{solution} 
        %s
    \end{solution}
    """ % (str(points), instructions, problem, solution)
    return code

if __name__ == "__main__":
    print(problem("test", "fasd", "asdfasd", 10))





