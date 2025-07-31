temp_in_F = int((input("Please type in a temperature in Faherenheit: ")))
temp_in_C = (temp_in_F - 32) * (5/9)
print(f"{temp_in_F} degrees Fahrenheit is {temp_in_C} degrees Celsius")
if temp_in_C < 0:
	print("It's freezing!")
	