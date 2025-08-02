print("Welcome to the burger ordering service")
print("price list: ")
print("Mini Burger(M): $5")
print("Normal Burger(N): $8")
print("Large Burger(L): $10")
print("Add Mushroom: For Mini and Normal burger = $1, For Large = $2")
print("Extra cheese: $1")

price = 0
size = input("What burger size do you want: ")
if size == "M":
	mushroom = input("Do you want mushroom added(y or n): ")
	cheese = input("Do you want mushroom added(y or n): ")
	if mushroom == "y":
		price = 5 + 1
	if cheese == "y":
		price = price + 1
	print(f"Total price of your order is ${price}")

		

