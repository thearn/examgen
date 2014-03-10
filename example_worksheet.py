from examgen import worksheet, make_quotient_rule_prob

# make an exam with a filename and title
myexam = worksheet("worksheet", "Example Worksheet 1", savetex=True)

# add some problem sections 
myexam.add_section("Linear equations", 20, "Linear equations",
                   "Solve the following equations for the specified variable.")
myexam.add_section("Quadratic equations", 20, "Quadratic equations",
                   "Solve the following quadratic equations.")
myexam.add_section(make_quotient_rule_prob,10, "Differentiation", 
                  "Compute each derivative", ["x", "y", "z"])

# generate the exam and solutions pdf
myexam.write()