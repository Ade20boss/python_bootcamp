from logo import logo
# Define the alphabet used for encryption/decryption (A-Z, digits, punctuation, symbols, and space)
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,!?;:'\"-_/\\@#$%^&*()[]{}+=<>~`|")
alphabet.append(' ')  # Add space character explicitly at the end



print("WELCOME TO THE CAESER CIPHER")

# Function to encrypt a message with Caesar cipher
def encrypt(message, shift_number):
	message = message.upper()  # Convert all characters to uppercase
	encrypted_list = []  # Store encrypted characters here

	# Loop through each character in the input message
	for char in message:
		if char in alphabet:  # Encrypt only if character exists in the defined alphabet
			old_index = alphabet.index(char)  # Get the current index of the character
			new_index = (old_index + shift_number)  # Apply the shift

			# If new index goes beyond the alphabet length, wrap it around
			if new_index > len(alphabet) - 1:
				while new_index > len(alphabet) - 1:
					new_index = new_index - len(alphabet)
				encrypted_list.append(alphabet[new_index])  # Append the wrapped character
			# If new index is valid (within range), just append
			elif new_index <= len(alphabet)-1:
				encrypted_list.append(alphabet[new_index])

	# Join the encrypted characters into a string
	encrypted_string = ''.join(encrypted_list)
	print(f"Your encoded message is {encrypted_string}")  # Print final encrypted message

# Function to decrypt an encrypted message
def decrypt(text, shift_value):
	text = text.upper()  # Convert all characters to uppercase
	decrypted_list = []  # Store decrypted characters here
	# Loop through each letter in the encrypted text
	for letter in text:
		if letter in alphabet:  # Decrypt only if character exists in the defined alphabet
			test_index = alphabet.index(letter)  # Get current index of encrypted character
			real_index = test_index - shift_value  # Reverse the shift to find original index
			# If index is valid (non-negative and within range), append directly
			if 0 <= real_index <= (len(alphabet)-1):
				decrypted_list.append(alphabet[real_index])
			# If index is negative, keep adding length until it wraps around
			elif real_index < 0:
				while real_index < 0:
					real_index = real_index + len(alphabet)
				decrypted_list.append(alphabet[real_index])
			# If index is still too high, reduce until it fits in range
			elif real_index > len(alphabet) - 1:
				while real_index > len(alphabet) - 1:
					real_index = real_index - len(alphabet)
				decrypted_list.append(alphabet[real_index])

	# Join decrypted characters into a string
	decrypted_string = ''.join(decrypted_list)
	print(f"This is your decrypted text: {decrypted_string}")  # Print final decrypted message



print(logo)
while True: 
	# Display menu for user
	print("Menu")
	print("1. ENCRYPT")
	print("2. DECRYPT")
	print()
	# Input validation loop for menu choice
	while True:
		user_choice = input("Enter your choice(1 or 2): \n ")
		if user_choice == "1" or user_choice == "2":
			break  # Valid choice, exit loop
		else:
			print("Invalid input")  # Repeat if invalid

	# If user selects ENCRYPT option
	if user_choice == "1":
		user_message = input("Enter message to encrypt: ")  # Get plain message
		caeser_shift = int(input("Enter shift number: "))  # Get shift number
		encrypt(user_message, caeser_shift)  # Call encrypt function

	# If user selects DECRYPT option
	elif user_choice == "2":
		cipher_message = input("Enter encrypted text to decrypt: ")  # Get cipher text
		cipher_number = int(input("Enter shift number: "))  # Get shift number
		decrypt(cipher_message, cipher_number)  # Call decrypt function

	while True:
		again = input("Enter 'y' to go again and 'n' to quit: \n").lower()
		if again == 'y' or again =='n':
			break
		else:
			print("Invalid input")
	if again =="y":
		print()
		continue
		
	else:
		break
print()
print("Thanks for using the caeser cipher, See you next time")
exit()

