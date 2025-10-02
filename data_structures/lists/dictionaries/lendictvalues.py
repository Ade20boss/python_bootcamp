import copy
def value_length(p_dict):
	for key, value in (p_dict.items()):
		p_dict[key] = {value: len(value)}
	print(p_dict)
names_dict = {
    1 : "Elshad",
    2 : "Renad",
    3 : "Johanna",
    4 : "Appmillers"
}
value_length(names_dict)

def remove_empty_items(p_dict):
    # TODO
    new_dict = {}
    if None in p_dict.items():
        print(p_dict)
    else:
        for key, value in p_dict.items():
            new_dict[key] = value
            if value == None or key == None:
                del new_dict[key]
        print(new_dict)
    


custom_dict = {
    "name" : "Elshad",
    "age" : None,
    "city" : None
}

remove_empty_items(custom_dict)

#Referencing dictionaries:
'''
When we create a  dictionary and assign it to a variable, the variable stores the dictionary 
now when we assign this dictionary variable to another variable, both variable will now be pointing
towards the same dictionary, so any changes made to the new variable will affect the original dictionary:
'''
person = {
    "name": "Daniel",
    "Age": 20,
    "city": "London"
    }

new_person = person #So the new_person and person are referring to the same dictionary
new_person["city"] = "Berlin"
print(person["city"])
print(new_person["city"])

#So we have effectively created two variable that point towards the same dictionary and any changes are centralized
#To separate the dictionaries we can use the copy method to create a copy of the dictionary:

"""
copy method:
This creates an entirely new dictionary in the memory but it's a shallow copy
A shallow copy means that it only copies the reference to the dictionary items, not the items themselves
but it wouldn't really have an effect if we were dealing with immutable data types like strings or numbers as the keys to the value
and also if the values are mutable data types like lists or dictionaries, if we were to do top level changes like reassigning a new list, then
it wouldn't affect the original dictionary but if were were to edit the mutable data types inside the dictionary or list, then it would affect the original dictionary
Bottom line: We should only use the copy method if we're dealing with immutable data types like str and int as values of keys in dictionaries
"""
old_person = person.copy()

"""
DEEP COPY:
The deep copy method creates a new dictionary in the memory and it copies all the items in the dictionary recursively,
meaning it creates a copy of the items inside the dictionary as well not just references to them
so if we were to change the items in the new dictionary, it wouldn't affect the original dictionary
It should be used when we're dealing with mutable data types like lists or dictionaries as values of keys in dictionaries
"""
city_list = ["London", "Berlin", "Paris"]
language_list = ["English", "German", "French"]
name_list = ["Daniel", "Elshad", "Renad"]
person2 = {
    "name": name_list,
    "city": city_list,
    "language": language_list
}

new_person2 = copy.deepcopy(person2), #With this we can do almost anyhow we want and we won't have any side effects
#because we have created an entirely new dictionary in the memory not just a reference to the original dictionary

