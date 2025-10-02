def group_types(custom_list):
	new_dict = {}.fromkeys(custom_list)
	for i in new_dict:
		if isinstance(i, str):
			new_dict[i] = "String"
		elif isinstance(i, int):
			new_dict[i] = "Integer"
	return new_dict



list1 = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
print(group_types(list1))
