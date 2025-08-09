def count_words(p_list):
	temp=''
	count = 0
	for i in range(len(p_list)):
		temp = p_list[i]
		if len(temp) >= 2 and temp[0] == temp[-1]:
			count += 1
	return count

list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
print(count_words(list1))