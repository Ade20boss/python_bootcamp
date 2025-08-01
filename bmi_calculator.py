height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
BMI = weight / height
print(f"Your BMI is {BMI}kg/m2")
if BMI < 18.5:
	print("You are underweight")
elif BMI > 18.5:
	if BMI < 25:
		print("Your weight is normal")
elif BMI > 25:
	if BMI < 30:
		print("You are Overweight")
elif BMI > 30:
	if BMI < 35:
		print("You are obese")