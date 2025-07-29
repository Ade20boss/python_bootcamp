print("Welcome to this simple calculator")
num1 = float(input("Please type in the first number: "))
num2 = float(input("Please type in the second number: "))
print("Pkease choose the operation you want to perform")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4.DIVISION")
operation = input("operation(1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
if operation == "1":
	result = num1 + num2
	print(f"The result of {num1} + {num2} is {result}")
elif operation == "2":
	result = num1 - num2
	print(f"The result of {num1} - {num2} is {result}")
elif operation == "3":
	result = num1 * num2
	print(f"The result of {num1} * {num2} is {result}")
elif operation == "4":
		if num2 != 0:
			result = num1 / num2
			print(f"The result of {num1} / {num2} is {result}")
		else:
			print("Error: Division by zero is not allowed.")
else:
	print("Invalid operation. Please choose 1, 2, 3, or 4.")
		

