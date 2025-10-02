#FORWARD DICTIONARY TRAVERSAL AND CHECKING IF A KEY EXISTS:
test_dictionary = {
	"Daniel": "A nerdy computer scientist", 
	"Habeeb": "I want to call him an engineer but i mean, really??",
	"Application": "Basically a program that's downloaded by users to run on a device",
	1: "Literally a single unit",
	}
for item in test_dictionary:
	if item == "Daniel":
		print("It exists in the dictionary")
		print(test_dictionary[item])

my_dict = {
    "name": "Edy",
    "age":30, 
    "salary": 5000, 
    "city": "London"
}
# TODO: Rename Key
removed = (my_dict.pop("city"))
my_dict["address"] = removed
print(removed)
print(my_dict)