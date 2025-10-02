
def concatenate(custom_dict1, custom_dict2, custom_dict3):
	new_dict = {}
	dictionaries = [custom_dict1, custom_dict2, custom_dict3]
	for dic in dictionaries:
		new_dict.update(dic)
	return new_dict

dict1={1: "one", 2: "two"}
dict2={3: "three", 4: "four"}
dict3={5: "five", 6: "six"}

print( concatenate(dict1, dict2, dict3))