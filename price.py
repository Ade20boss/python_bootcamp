copies = int(input("How many books are you buying(remember you get 40% discount as a bookstore): "))
price_per_book = 24.95-((40/100)*24.95)
price_of_shipping = (0.75*(copies-1)) + 3
total = round((price_per_book*copies) + (price_of_shipping), 2)
print(f"The total cost of {copies} copies is ${total}")