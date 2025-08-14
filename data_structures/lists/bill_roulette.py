import random 
names = (input("Enter the names separated by commas: ")).split(",")
payer = random.choice(names)
print(f"{payer} is going to pay for the meal today!")

