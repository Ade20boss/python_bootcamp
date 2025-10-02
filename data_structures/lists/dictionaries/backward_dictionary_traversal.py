#BACKWARD DICTIONARY TRAVERSAL
test_dictionary = {
	"Daniel": "A nerdy computer scientist", 
	"Habeeb": "I want to call him an engineer but i mean, really??",
	"Application": "Basically a program that's downloaded by users to run on a device",
	1: "Literally a single unit",
	}
key_list = []
for key in test_dictionary:
	key_list.append(key)
for i in range(1, len(key_list) + 1):
	i = i * -1
	print(key_list[i], test_dictionary[key_list[i]])
	