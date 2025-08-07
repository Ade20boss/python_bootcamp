import random
while True:
	dice1_number = random.randint(1, 6)
	print(f"Dice1: {dice1_number}")
	dice2_number = random.randint(1, 6)
	print(f"Dice2: {dice2_number}")
	choice = input("Roll dice again? (Y/N)").upper()
	if choice == "Y":
		continue
	elif choice == "N":
		break
	else:
		print("Invalid choice")
		break

