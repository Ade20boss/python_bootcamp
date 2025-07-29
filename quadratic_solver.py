from math import sqrt
def quadratic_solver():
	a = int(input("Value of a: "))
	b = int(input("Value of b: "))
	c = int(input("Value of c: "))
	solution1 = ((b * -1) + (sqrt((b**2)- (4*a*c)))) /(2*a)
	solution2 = ((b * -1) - (sqrt((b**2)- (4*a*c)))) /(2*a)
	print(f"The roots are {solution2} and {solution1}")
	# This function solves a quadratic equation of the form ax^2 + bx + c = 03
quadratic_solver() # Call the function to solve the quadratic equation
