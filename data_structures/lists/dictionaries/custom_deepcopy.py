def deep_copy(dict1):
    new_dict = {}
    for key, value in dict1.items():
        new_dict[key] = value
    return new_dict

dict1 = {1: "one", 2: "two", 3: "three"}
dict2 = deep_copy(dict1)
dict2[4] = "four"
print(dict2)