def generate_dictionary(n):
	dictionary = {}
	for i in range(1, n+1):
		dictionary[i] = i*i
	print(dictionary)
generate_dictionary(5)