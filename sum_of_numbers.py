print("Choose the type of sum to calculate:")
print("1 - Sum of all numbers")
print("2 - Sum of even numbers")
print("3 - Sum of odd numbers")

choice = input("Enter your choice (1/2/3): ")
start = int(input("Enter start: "))
stop = int(input("Enter stop: "))

num_sum = 0

if choice == "1":
    for i in range(start, stop + 1):
        num_sum += i
elif choice == "2":
    for i in range(start, stop+1):
        if i % 2 == 0:
            num_sum += i
elif choice == "3":
    for i in range(start, stop+1):
        if i % 2 != 0:
            num_sum += i
else:
    print("Invalid choice.")
    exit()

print(f"The result is: {num_sum}")
