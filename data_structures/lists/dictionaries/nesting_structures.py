def add_new_user(lcustom_string, list1, number):
	dictionary = {}
	dictionary["user_name"] = lcustom_string
	dictionary["favorite_languages"] = list1
	dictionary["Experience"] = number

	print(dictionary)
add_new_user("david", ["Python", "Java", "C#", "Ruby"], 10)

#Nesting list inside dictionary
programming_languages = {
	"Daniel": ["Python", "Java", "C#", "Ruby"], #The value of key "Daniel" is set to a list
	"Habeeb": "Matlab"
	}

#Nesting dictionary inside dictionary:
programming_languages = {
	"Daniel": {"favourite programming languages(s)": ["Python", "Java", "C#", "Ruby"],
			"Experience" : 10
			},
	"Habeeb": {"favourite_languages": ["Python", "Matlab"],
			"Experience": 0
			},
	
	}

#Nesting dictionary inside list
programming_languages = [

	{
	"user_name": "Daniel",
	"favourite_languages": ["Python", "Java", "C#", "Ruby"],
	"Experience" : 10
    },

	{
	"user_name": "Habeeb",
	"favourite_languages": ["Python", "Matlab"],
	"Experience": 0
    }

	]

print(add_new_user("Edy", ["Java", "Kotlin", "Swift"], 10))


#HANDLING MISSING KEYS IN DICTIONARY
items = {
	"computer": 10,
	"printer": 8,
	"mouse": 15,
	"webcam": 12,
	"router": 10,
	}
'''
One method to handling missing keys is to use the dictionary get method which
accesses the value of a key in a dictionary and we can use it to handle missing key error
by using additional parameters when it is called and it returns none if the key doesn't exist
'''
quantity = items.get("microphone", "The item does not exist")
print(f"Number of microphones in the store: {quantity}")#This displays a message to the screen since microphone is not a valid key in the dictionary

'''
Another method is using the setdefault method which looks for a key in a dictionary and 
if the key doesn't exist, it assigns it to a default value which is usually none but we can specify
the value we want to assign to it. Note that it doesn't apply to elements that are already in the dictionary
If the key is in the dictinonary, the setdefault method doesn't work.
'''
quantity1 = items.setdefault("microphone", 0)#Note we can specify how much we want
print(f"Nimber of microphones in the store: {quantity}")#This creates a new key "microphone" and assigns 0 as a value to it since the key doesn't exist in the dictionary




