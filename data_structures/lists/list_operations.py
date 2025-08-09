#SLICING:
names = ["John", "Jane", "Kane", "Marvelous"]
names_with_j = names[:2]
print(names_with_j)
name = names[3][:6]
print(name)

names[1:3] = ["Daniel", "Franchesca"]
print(names)

#CONCATENATE LISTS
list1 = [1, 2, 3, 4, 5, 6]
list2 = [7, 8, 9, 10, 11]
list3 = list1 + list2
print(list3)

#*operator on strings: This allows the repition of items a certain number of times
list1 = [1, 2]
list2 = list1 * 2
print(list2)

print(names[:-2])

#REVERSE A LIST:
custom_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
custom_list = custom_list[len(custom_list)::-1]
print(custom_list)


def reverse_a_list(lst):
	new_list = []
	for i in range(len(lst)):
		index = -i-1
		new_list.append(lst[index])
	lst[:] = new_list
	return lst

print(reverse_a_list(custom_list))

#LIST METHODS
#The index method specifies the index of a specified element in a string
animals =  ["cow", "goat", "horse", "mouse", "bear"]
print(animals.index("horse"))
#We can also modify the index method such that it finds the index of an item within a specific range:
print(animals.index("horse", 0, 4))#This looks for the item 'horse' within range of index 4-7

#The append method allows us to add an element add the end of the list:
animals.append('fox')#Add the item 'fox' to the list of animals

#The Extend moethod takes the work of the append method a step further
#by allowing us to also extend a list with another list:
animals2 = ["rabbit", "gazelle", "monkeys"]
animals.extend(animals2)#This extends the animals list with animals2 list, so basically it adds all the
#item in the animals2 list to the animals list

#The insert method allows us to insert an element into the specified index of a list:
animals.insert(2, 'warthog')#This adds 'warthog' to index 2 of the animals list without overwriting what was
#originally at index 2

#The remove method removes the specified item from the list but removes only the first occurence of that item from the list
animals.remove("horse")

#The count method returns the number of times that the specified item appears in the list:
count = animals.count("bear")

#The pop method removes the element in the specified index and returns the elemnt. Note that this method takes 
#in the index of the element as argument and not the element itself:
item_extracted = animals.pop(3)

#The reverse method in python helps us reverse the list: It doesn't return anything
animals.reverse()

#The sort method allows us to sort the items in a list, we can do it in an ascending or descending order:
numbers = [1, 2, 5, 6, 4, 3, 8, 9, 11, 13, 10, 12]
numbers.sort()#This sorts the lnumbers list in ascending order
numbers.sort(reverse = True)#This sorts the list in descending order

#The copy method returns a copy of a list:
new_numbers = numbers.copy()#This is pretty useless and not memory efficient in my opinion because we
#can do the same thing it does using the assignment assignment:
new_numbers = numbers#But the problem with this is that doing this, we're referencing the assigned list
#So i guess the copy method isn't all that useless any ways

#The clear method deletes all items in a list:
numbers.clear()




	

	

