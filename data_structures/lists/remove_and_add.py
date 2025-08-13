'''
Remove an element at index 4 in a given list and add it to the 2nd position and at the end of the list.
'''
custom_list = [10, 44, 57, 99, 11, 33, 84]
temp = custom_list[4]
custom_list.remove(custom_list[4])
custom_list.insert(2, temp)
custom_list.insert(len(custom_list), temp)
print(custom_list)