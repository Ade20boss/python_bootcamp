'''
the fromkeys() method allows us to create a dictionary fro m another dat structure like a list
Say we're using a list, it creates a new dictionary and assigns the keys of the dictionary to elements
of the list
'''

custom_dict = {
	0: "zero",
	1: "one",
	2: "two",
	3: "three",
	4: "four",
	5: "five",
	6: "six",
	}

devices_list = ["phones", "tablets", "computers", "TVs"]

new_dict = {}.fromkeys(devices_list)#This creates a new dictionary that uses the elements of the list as keys
#and by default their values are assigned as NONE

new_dict = {}.fromkeys(devices_list, 0)#We can assign another default value to each keys
print(new_dict)

'''
The keys method is typically used to iterate over the keys of a dictionary and returns a VIEW OBJECT
a view object is similar to a list but it is not mutable. It's a copy representation of elements in a dictionary
'''
keys = custom_dict.keys()
print(keys)

#The items method for dictionaries allows us to iterate over both the key and the value of each keys
for key, value in custom_dict.items():
	print(key, value)

#DICTIONARY UPDATE METHOD: This method allows us to update the components of a dictionary wihth
#the components of another, but note tha duplication of keys is not allowed in dictionaries
custom_dict2 = {
	7: "Seven",
	8: "eight",
	9: "nine",
	1: "new_one",
	2: "new_two"
	}

custom_dict.update(custom_dict2)#This updates the contents of the custom_dict by adding three new key value pairs
#and also updating the values of 1 and 2 in the dictionary cause they exist in the dictionary
for i, j in custom_dict.items():
	print(i, j)

#There's the union operator and the augmented union version that to my understanding does the same thing as the update method

#We can use the values method to return a view object of the values of a dictionary, kind of like the keys method
print(custom_dict2.values())
#by using the in operator we can check if a value exists in a dictionary:
print("one" in custom_dict.values())


search = input("What values are you looking for in the dictionary: ").lower()
#This code allows us to find all occurences of the value accross the entire dictionary
for key, value in custom_dict.items():
	if value == search:
		print(f"{search} is found with the key {key}")
	




