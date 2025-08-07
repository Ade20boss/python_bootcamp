print("This is an interesting fizzbuzz game that allows you to play the fizzbuzz game for an arbotrary number of values")
number_of_values = int(input("What is the range of values for the fizzbuzz game: "))
for i in range (number_of_values+1):
	if i % 5 == 0 and i % 7 == 0:
		print("FizzBuzz")
	elif i % 5 == 0:
		print("Fizz")
	elif i % 7 == 0:
		print("Buzz")
	else:
		print(i)