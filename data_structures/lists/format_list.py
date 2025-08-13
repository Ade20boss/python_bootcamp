custom_list = [1, 2, 3, 4, 5]
output = []
for i in custom_list:
	output.append(str(i))
	
custom_string = " | ".join(output)#Join function only works with a string list
print(custom_string)
