def doc_parts(title="", author=""):
    start="""
    \documentclass{article}
    \usepackage{amsfonts}
    \usepackage{amsmath,multicol,eso-pic}
    \\begin{document}
    """

    if title:
        start = start + "\\title{%s} \n \date{\\vspace{-5ex}} \n \maketitle" % title

    end="""
    \end{document}
    """
    return start, end

def section_parts(title, instr=""):

    section_start="""
    \section{%s}
    %s
    \\begin{multicols}{2}
    \\begin{enumerate}
    """ % (title, instr)

    section_end="""
    \end{enumerate}
    \end{multicols}
    """
    return section_start, section_end