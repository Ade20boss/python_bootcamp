def third_list(p1_list, p2_list):
	new_list = []
	for i in range(len(p1_list)):
		if i % 2 !=0:
			new_list.append(p1_list[i])
	for j in range(len(p2_list)):
		if j % 2 == 0:
			new_list.append(p2_list[j])
	return new_list

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]

third_list(list_one, list_two)

