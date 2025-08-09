
#STRING PARSING:
'''
This basically means looking into a string and checking for a substring
and this is usually done using different string methods
For example, say we're given a string as follows:
"From example.email@edu.co.uk Sat Sep 5 09:14:16 2021" and we want to 
extract only the domain of the email; we can just use the find method and
also string slicing:
'''
data = "From example.email@edu.co.uk Sat Sep 5 09:14:16 2021"
index_of_at = data.find("@")
space_after_at = data.find(' ', index_of_at)
extracted_data = data[index_of_at:space_after_at]
print(extracted_data)

# -------------------------------
# split() method
# -------------------------------
# Purpose: Breaks a string into a list of substrings, based on a separator.
# Syntax: string.split(separator, maxsplit)
# - separator (optional): Where to split. Default is whitespace.
# - maxsplit (optional): Max number of splits. Default -1 (no limit).
# Returns: A list of substrings.
# Example:
text = "apple,banana,cherry"
result = text.split(",")  # ['apple', 'banana', 'cherry']

# -------------------------------
# join() method
# -------------------------------
# Purpose: Combines a list (or iterable) of strings into one string,
# inserting a separator between each element.
# Syntax: separator.join(iterable)
# - separator: String to insert between elements.
# - iterable: Sequence of strings (e.g., list, tuple).
# Returns: A single string.
# Example:
fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)  # "apple, banana, cherry"
# Quick Tip:
# split()  → String → List
# join()   → List → String


# ----------------------------------------------------
# f-strings (formatted string literals) in Python
# ----------------------------------------------------
# Purpose: Insert variables or expressions directly into strings.
# Syntax: f"string {expression}"
# - Place variables or expressions inside curly braces {}.
# - Python will replace them with their values.
#
# Formatting numbers:
# {variable:#x} → Format integer as hexadecimal with '0x' prefix.
# Common format codes:
#   d  → Decimal integer
#   x  → Hexadecimal (lowercase, no prefix)
#   X  → Hexadecimal (uppercase, no prefix)
#  #x  → Hexadecimal (lowercase, with '0x' prefix)
#  #X  → Hexadecimal (uppercase, with '0X' prefix)
#   b  → Binary
#   o  → Octal
#
# Example:
error_no = 45457984738
name = "Daniel"
print(f"Hey {name}, there is a {error_no:#x} error!")
# Output: Hey Daniel, there is a 0xa949d9bf2 error!

custom_string = 'X-MAPDS-Confidence:0.8475' 
index_of_colon = custom_string.find(":")
extracted_data = custom_string[index_of_colon+1:]
extracted_data = float(extracted_data)
print(extracted_data)


