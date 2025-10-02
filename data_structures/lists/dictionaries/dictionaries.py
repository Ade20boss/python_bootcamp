'''
In a literal dictionary if we look up a word, we see that the word is paired with it's corresponding definition
This is a similar concept in python, a dictionary is basically a set of key value pairs , where the key is an entity and
the value is some property that relates to that entity. So if we were to implement a literal dictionary in python, the
key would be the word and the value would be the definition accompanying the word.
When accessing a dictionary, we use the key unlike lists which use the index for accessing. 
'''

#DICTIONARY CREATION AND ACCESSING:
test_dictionary = {
	"Daniel": "A nerdy computer scientist", 
	"Habeeb": "I want to call him an engineer but i mean, really??",
	"Application": "Basically a program that's downloaded by users to run on a device",
	1: "Literally a single unit",
	}
#test_dictionary = {}#This allows us to clear out every key value pair in the dictionary
#print(test_dictionary["Daniel"])#This allows us to access the value of the key specified

#Inserting/Updating elements of a string
test_dictionary["Rene Descartes"] =  "The man i consider to be the single individual that bridged the gap between algebra and geometry" #This allows us to add a key value pair to the dictionary
test_dictionary["Daniel"] = "The superior being, one who has transcended humanity" #This updates the values of the key "Daniel"
#So with the assignment operator we can update and insert elements in a dictionary
#print(test_dictionary)

#Deleting an item from a dictionary:
#The dictionary built in pop function removes an item with the provided key and then
#returns the removed item:
'''
in the case where we have a wrong key passed into the pop function, to prevent an error, we
can provide a default value that get's printed instead of an error:
'''
print(test_dictionary.pop(1), "The result does not exist")#So in this case, we don't get an error if the key doesn't exist, we simply get "The key doesn't exist" printed to the console

'''
Another way to remove an item from a dictionary is using the popitem method that
removes the last inserted key value pair from the dictionary and returns this removed key value pair
'''
print(test_dictionary.popitem())

#Another method is using the del keyword, it removes the key value pair specified but doesn't return anything
del test_dictionary["Daniel"]
#Another one is using the clear method that erases everything in the dictionary
test_dictionary.clear()
#Note, in and not in operators work with keys when working with dictionaries

#












