def square_list(p_list):
	for index in range(len(p_list)):
		p_list[index] = p_list[index] ** 2
	return p_list

print(square_list([1, 2, 3, 6, 7, 9]))