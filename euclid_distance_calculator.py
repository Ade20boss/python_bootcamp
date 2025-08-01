import math
print("Welcome to Euclid distance calculator")
distance_square = 0
while True:
	number_of_dimensions = int(input("Enter number of dimensions: "))
	if number_of_dimensions > 0:
		x_coords = []
		y_coords = []

		for i in range(number_of_dimensions):
			x = float(input(f"Enter x{i + 1}"))
			x_coords.append(x)

		for i in range(number_of_dimensions):
			y = float(input(f"Enter y{i + 1}"))
			y_coords.append(y)

		for x, y in zip(x_coords, y_coords):
			distance_square += (x-y)**2

		euclid_distance = round(math.sqrt(distance_square), 2)
		break
	elif number_of_dimensions <= 0:
		print("Invalid number of dimensions")
