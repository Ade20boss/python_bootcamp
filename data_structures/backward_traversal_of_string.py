string = input("Enter a string: ")
index = -1
stop_point = (-1 * (len(string)))-1
while index > stop_point:
    letter = string[index]
    print(letter)
    index -= 1