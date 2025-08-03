print("Welcome to leap year checker")
year = int(input("Enter year to check: "))
if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print(f"{year} is a leap year")
	
