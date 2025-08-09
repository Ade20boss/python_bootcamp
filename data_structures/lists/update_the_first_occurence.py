lst = [10, 10, 5, 15, 50, 50, 20]
for i in range(len(lst)):
	if lst[i] == 50:
		lst[i] = 5
		break#We can just remove this line if we want to replace all occurences of 50
print(lst)