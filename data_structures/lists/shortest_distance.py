from email.charset import SHORTEST


def shortest_distance(custom_list, first_word, second_word):
	index1 = []
	index2 = []
	minimum = float("inf")
	for i, w in enumerate(custom_list):
		if w == first_word:
			index1.append(i)
		elif w == second_word:
			index2.append(i)
	if index1 == [] or index2 == []:
		return None
	for i in index1:
		for j in index2:
			dist = abs(i-j)
			if dist < minimum:
				minimum = dist
	return minimum

list1 = ['kiwi', 'mango', 'banana', 'cherry', 'grape', 'peach', 'fig', 'fig', 'banana', 'kiwi',
 'mango', 'lemon', 'date', 'date', 'fig', 'grape', 'cherry', 'fig', 'grape', 'kiwi',
 'banana', 'lemon', 'fig', 'lemon', 'fig', 'peach', 'cherry', 'mango', 'peach', 'kiwi',
 'grape', 'fig', 'kiwi', 'date', 'lemon', 'lemon', 'banana', 'banana', 'peach', 'cherry',
 'date', 'date', 'apple', 'lemon', 'grape', 'date', 'peach', 'apple', 'date', 'peach']

min_dist = shortest_distance(list1, "mango", "apple")
print(min_dist)


	