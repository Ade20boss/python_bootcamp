value_of_gift = float(input("Value of gift: "))
if value_of_gift < 5000:
	print("No tax!")
elif value_of_gift >= 5000 and value_of_gift <= 25000:
	if value_of_gift == 5000:
		print("Amount of tax: 100.0 euros")
	elif value_of_gift > 5000 and value_of_gift <= 25000:
		tax1 =  (100.0 + (value_of_gift - 5000) * 0.08)
		print(f"Amount of tax: {tax1} euros")

elif value_of_gift >= 25000 and value_of_gift <= 55000:
	if value_of_gift == 25000:
		print("Amount of tax: 1700.0 euros")
	elif value_of_gift > 25000 and value_of_gift <= 55000:
		tax2 =  (1700.0 + (value_of_gift - 25000) * 0.1)
		print(f"Amount of tax: {tax2} euros")

elif value_of_gift >= 55000 and value_of_gift <= 200000:
	if value_of_gift == 55000:
		print("Amount of tax: 4700.0 euros")
	elif value_of_gift > 55000 and value_of_gift <= 200000:
		tax3 =  (4700.0 + (value_of_gift - 55000) * 0.12)
		print(f"Amount of tax: {tax3} euros")

elif value_of_gift >= 200000 and value_of_gift <= 1000000:
	if value_of_gift == 200000:
		print("Amount of tax: 22100.0 euros")
	elif value_of_gift > 200000 and value_of_gift <= 1000000:
		tax4 = (22100 + (value_of_gift - 200000) * 0.15)
		print(f"Amount of tax: {tax4} euros")

elif value_of_gift >= 1000000:
	if value_of_gift == 1000000:
		print("Amount of tax: 142100.0 euros")
	elif value_of_gift > 1000000:
		tax5 = (142100 + (value_of_gift - 1000000) * 0.17)
		print(f"Amount of tax: {tax5} euros")

