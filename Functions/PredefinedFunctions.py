myString = "Hello world"

# lenght function
lengthOfString = len(myString)
print("Length of the string is: ", lengthOfString)

# Lower case function
lowerCaseofString = myString.lower()
print("Lower case of string is: ", lowerCaseofString)

# Upper case function
upperCaseofString = myString.upper()
print("Upper case of string is: ", upperCaseofString)

# Title function     ---> Makes first letter of each word as capital..!!!
titleofString = myString.title()
print("Title of string is: ", titleofString)

# Concatenate fucntion
# Concatenate string and integeter ( string + int ) will not work..!!!!!!  e.g: "5" + 2 (throw error)
str1 = "My name is"
str2 = "Naresh"
concatinateStrings = str1 + str2
print("Strings concatenate: ", concatinateStrings)

# String function  --> Removing leading and trailing spaces
string = "   Hello World        "
print("String value without strip: ", string)
strippingMyString = string.strip()
print("After using strip function: ",strippingMyString)

# Replace function
beforeReplacce = "Hello world and giving aganin Hello world"
afterReplaced = beforeReplacce.replace("world", "world123")
print("After replacing string is: ", afterReplaced)

## Replace example
string = "I Love India"
replaceSpace = string.replace(" ", "_")
print("Replaced string is: ", replaceSpace)

# Indexing   --> Indexing always starts from 0
word = "India"
print("1st index:", word[0])
print("2nd index:", word[1])
print("3rd index:", word[2])
print("4th index:", word[3])
print("5th index:", word[4])

print("-"*12)
## Here we can give in reverse order alse, indexing start from '-1' if you want to calculate from last
print("5th index:", word[-1])
print("4th index:", word[-2])
print("3rd index:", word[-3])
