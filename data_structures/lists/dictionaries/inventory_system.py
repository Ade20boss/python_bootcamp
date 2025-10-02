admin_password = "h7666hukyddxf"
stock = {
    "computer" : [1, 10, 10000],
    "monitor" : [2, 10, 6000],
    "keyboard" : [3, 10, 4000],
    "mouse" : [4, 10, 1500],
    "hdmi cable" : [5, 10, 200],
    "dvd drive" : [6, 10, 150],
    "usb cable" : [7, 10, 100]
}
choice = input("Are you an administrator?(y/n): ")
if choice == "y":
    while True:
        password = input("Enter password: ")
        if password == admin_password:
            break
        print("Incorrect password")
    print("Welcome admin")
    print("Please choose an option")
    print("1: Add item")
    print("2: Delete item")
    print("3: Edit item")
    print("4: Exit")
    while True:
        input_option = int(input("> "))
        if input_option == 1:
            item_name = input("Enter item name: ")
            if item_name in stock:
                print("Item already exists")
            else:
                item_quantity = int(input("Enter item quantity: "))
                item_price = int(input("Enter item price: "))
                new_id = max(item[0] for item in stock.values()) + 1
                stock[item_name] = [new_id, item_quantity, item_price]
        elif input_option == 2:
            item_name = input("Enter item name: ")
            if item_name in stock:
                del stock[item_name]
            else:
                print("Item not found")
        elif input_option == 3:
            item_name = input("Enter item name: ")
            if item_name in stock:
                change_option = int(input("1: Increase quantity\n2: Decrease quantity\n3: Edit price\n> "))
                if change_option == 1:
                    increase = int(input("Enter increase quantity: "))
                    stock[item_name][1] += increase
                elif change_option == 2:
                    decrease = int(input("Enter increase quantity: "))
                    if stock[item_name][1] < decrease:
                        print("Error: Not enough stock to decrease")
                    else:
                        stock[item_name][1] -= decrease
                elif change_option == 3:
                    stock[item_name][2] = int(input("Enter new price: "))
            else:
                print("Item not found")
        elif input_option == 4:
            print("Exiting...")
            print("Thank you for using our service")
            exit()
        else:
            print("Invalid option")

elif choice == "n":
    total = 0
    prices = []
    keys = []
    options = {}
    print("Please add options from the list")
    for key in stock:
        print(str(stock[key][0]) + ": " + key + " - " + "$" + str(stock[key][2]))
    new_id = max(item[0] for item in stock.values()) + 1
    print(str(new_id) + ": " + "View Cart")
    print(str(new_id + 1) + ": " + "Remove item from Cart")
    print("0: to finish")

    for values in stock.values():
        prices.append(values[2])
    for key in stock:
        keys.append(key)

    while True:
        option = int(input("> "))
        if option == 0 or option == new_id:
            if option == 0:
                break
            else:
                print("Your cart:")
                for item, qty in options.items():
                    print(f"{item} x{qty} - ${stock[item][2] * qty}")
                print(f"Total price: ${total}")
                continue

        if option == new_id + 1 and options != {}:
            print(f"Your cart {options}")
            while True:
                removed = input("Enter item to remove: ")
                if removed in options.keys():
                    break
                else:
                    print("Invalid item")
            while True:
                num = int(input(f"You have {options[removed]} of that item in the cart, how many do you want to remove: "))
                if options[removed] >= num:
                    break
                else:
                    print("Invalid number")
            options[removed] = options[removed] - num
            if options[removed] <= 0:
                del options[removed]
            total -= stock[removed][2] * num
            stock[removed][1] += num
            continue
        elif option == new_id + 1 and options == {}:
            print("There's nothing in your cart")
            continue
        if 0 < option <= len(keys) and stock[keys[option - 1]][1] > 0:
            total += prices[option - 1]
            print(f"Adding {keys[option - 1]}")
            stock[keys[option - 1]][1] -= 1
            if keys[option - 1] in options.keys():
                options[keys[option - 1]] += 1
            else:
                options[keys[option - 1]] = 1
        elif len(keys) >= option > 0 == stock[keys[option - 1]][1]:
            print(f"{keys[option - 1]} is out of stock")
        else:
            print("Invalid option, Please try again")

    print("Your cart:")
    for item, qty in options.items():
        print(f"{item} x{qty} - ${stock[item][2] * qty}")
    print(f"Total price: ${total}")
    print("Thank you for using our services")

