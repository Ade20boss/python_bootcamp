my_dict = {
    3: "Three",
    5: "Five",
    9: "Nine",
    2: "Two",
    1 : "one",
    4: "Four"
}

print("Three" in my_dict) #in operator and not in operator by default works on keys not values
print("Three" in my_dict.values()) #The values method returns a view object of the values of a dictionary allowing us to use the in operator on the values
print(len(my_dict))#The len method returns the number of items in a dictionary(key and value are one time))
print(all(my_dict.values()))#The all method returns True if all the values of a dictionary are Truthy, and return false if any value if falsy(like 0, False, None, [])
print(any(my_dict.values()))#The any method returns True if any of the values of a dictionary are Truthy, and return false if all values are falsy(like 0, False, None, [])
print(sorted(my_dict))#This method returns a sorted list of the keys of a dictionary
print(sorted(my_dict.values()))#This method returns a sorted list of the values of a dictionary because we have added ".values()" at the end of the line
print(my_dict.get(54, "Does not exist"))#Returns the value of the key specified, if the key doesn't exist, it returns does not exist cause it has been specified'