import math
import random
print("Welcome to guessing game")

lower_bound = int(input("Enter lower bound(Please note; cannot be larger than upper bound: " ))
upper_bound = int(input("Enter upper bound(Please note, cannot be smaller than upper bound: "))

secret_number = random.randint(lower_bound, upper_bound)

chances = round(math.log(upper_bound - lower_bound + 1, 2))
print(f"You've only {chances} chances to guess the integer!")
count = 0

while chances > 0:
	count += 1
	user_input = int(input("Guess a number: "))
	if user_input == secret_number:
		print(f"Congratulations, you did it in {count} try")
	elif user_input < secret_number:
		print("You guessed too small!")
	elif user_input > secret_number:
		print("You guessed too high")
	chances -= 1

if chances <= 0:
	print(f"The number is {secret_number}")
	print("Better luck next time")
	quit()


	
	