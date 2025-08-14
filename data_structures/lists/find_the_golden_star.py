import random
def print_map(p_map):
	for row in p_map:
		formatted_list = []
		for item in row:
			formatted_list.append("{:2}".format(item))
			row_string = " ".join(formatted_list)
		print(row_string)

custom_map = ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
print("This is the initial map....")
print("There are three rows and three columns")
print_map(custom_map)

gold_row = random.randint(0, 2)
gold_column = random.randint(0, 2)
gold_position = str(gold_row+1) + str(gold_column + 1)
custom_map[gold_row][gold_column] = "⭐️"


while True:
	user_position = input("What do you think: Where is the golden star? Enter column choice and row choice side by side: ")
	if len(user_position) == 2 and user_position.isdigit():
		if 1 <= int(user_position[0]) <= 3 and 1 <= int(user_position[1]) <= 3:
			break
		else:
			print("Invalid input, Enter a valid input")
	else:
		print("Invalid input, Enter a valid input")

if gold_position == user_position:
	print("Congratulations, You found the golden star")
	print_map(custom_map)
else:
	print("Unfortunately you couldn't find it 🙁")
	user_row = int(user_position[0])-1
	user_column = int(user_position[1])-1
	custom_map[user_row][user_column] = "🆇"
	print_map(custom_map)







