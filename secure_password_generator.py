import random
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@',
    '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]

print("Welcome to password generator")
nr_of_letters = int(input("How many letters do you want in your password: "))
nr_of_symbols = int(input("How many symbols do you want in your password: "))
nr_of_numbers = int(input("How many numbers do you want in your password: "))
password = []
for char in range(1, nr_of_letters+1):
    password.append(random.choice(letters))
    
for sym in range(1, nr_of_symbols+1):
    password.append(random.choice(symbols))

for num in range(1, nr_of_numbers):
    password.append(random.choice(numbers_str))
    
random.shuffle(password)
password1 = ""
for i in password:
    password1 += i
print(f"Your newly generated passowrd is {password1}")

