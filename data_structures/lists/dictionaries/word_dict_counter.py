def count_character(custom_string):
	letters = []
	count = []
	my_dict = {}
	for letter in custom_string:
		letters.append(letter)
		count.append(custom_string.count(letter))
	for i in range(len(letters)):
		my_dict[letters[i]] = count[i]
	return my_dict



	
