def merge_dict(dict1, dict2):
    new_dict = dict1.copy()
    new_dict.update(dict2)
    return new_dict

dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

print(merge_dict(dict1, dict2))

"""
DEEP COPY:

"""
