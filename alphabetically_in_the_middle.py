a = input("Enter first letter:")
b = input("Enter second letter:")
c = input("Enter third letter:")
if (a > b and a < c) or (a < b and a > c):
	print(f"{a} is in the middle")	
elif (b > a and b < c) or (b < a and b > c):
	print(f"{b} is in the middle")
elif (c > a and c < b) or (c < a and c > b):
	print(f"{c} is in the middle")