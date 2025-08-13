def concatenate(p_list1, p_list2):
	new_list1 = []
	for i in range(len(p_list1)):
		print(i)
		if i == 0:
			new_list1.append(p_list1[i] + p_list2[i])
			new_list1.append(p_list1[i] + p_list2[i-1])
		if i == 1:
			new_list1.append(p_list1[i] + p_list2[i-1])
			new_list1.append(p_list1[i] + p_list2[i])
			break
	return new_list1

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list = concatenate(list1, list2)
print(new_list)