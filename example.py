from examgen import exam

# make an exam with a filename and title
myexam = exam("algebra1", "Algebra 101 exam 1", savetex=True)

# add some problem sections 
myexam.add_section("Linear equations", 20, "Linear equations",
                   "Solve the following equations for the specified variable.")
myexam.add_section("Quadratic equations", 20, "Quadratic equations",
                   "Solve the following quadratic equations.")

# generate the exam and solutions pdf
myexam.write()