def sum_average_and_count():
    count = 0
    sum1 = 0

    while True:
        p_num = input("Enter a number: ")
        if p_num == "done":
              break
        try:
             p_num = int(p_num)
        except ValueError:
            print("Error, Invalid input")
            continue
       
        
        count += 1
        sum1 += p_num
    average = sum1/count
    print(f"The sum of numbers is {sum1}")
    print(f"The number of numbers inputted is {count}")
    print(f"The average of the numbers is {average}")


    


