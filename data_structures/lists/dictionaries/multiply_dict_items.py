def dict_multiply(dictionary):
	multiply = 1
	for key in dictionary:
		multiply *= dictionary[key]
	print(multiply)


my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}

dict_multiply(my_dict)