custom_string = input("Enter a string: ")
for i in custom_string:
	if i == ".":
		custom_string = custom_string.replace(".", "!")
print(custom_string)