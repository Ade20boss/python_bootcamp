def print_pattern(n):
    # ----------------------------------------------------------
    # Purpose: Prints a star (*) pattern that first increases
    # in length, then decreases.
    #
    # Example (n = 5):
    # *
    # **
    # ***
    # ****
    # *****
    # ****
    # ***
    # **
    # *
    #
    # How it works:
    # 1. First loop: increment star count from 1 up to n
    # 2. Second loop: decrement star count from n-1 down to 1
    # ----------------------------------------------------------

    increment = 1           # Starting number of stars for the first loop
    decrement = n - 1       # Starting number of stars for the second loop

    # Increasing pattern
    for i in range(n):
        print("*" * increment)   # Multiply "*" by increment value
        increment += 1           # Increase star count by 1

    # Decreasing pattern
    for j in range(n):
        print("*" * decrement)   # Multiply "*" by decrement value
        decrement -= 1           # Decrease star count by 1



def print_square(length):
    for i in range(length):
        print("*" * length)

#print_square(7)

def print_rectangle(rows, column):
    for _ in range(rows):
        if rows == column:
            print("*" * rows)
        elif rows < column:
            high = column - rows
            print("*" * (rows+high))
        elif rows > column:
            low = rows-column
            print("*" * (rows-low))
print_rectangle(7, 6)
