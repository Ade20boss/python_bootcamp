def find_max(number_of_values):
	nums = []
	for i in range(number_of_values):
		try:
			num1 = int(input(f"Enter number{i + 1}: "))
		except ValueError:
			print("Enter valid numeric input")
			quit()
		nums.append(num1)
	max = nums[0]
	for i in nums:
		if i > max:
			max = i
	return max

number_of_values = int(input("How many numbers do you want to check: "))
output = find_max(number_of_values)
print(output)