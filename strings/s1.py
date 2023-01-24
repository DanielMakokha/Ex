# Write a program that asks the user to enter a string. The program should then print the
# following:

# (a) The total number of characters in the string
# (b) The string repeated 10 times
# (c) The first character of the string (remember that string indices start at 0)
# (d) The first three characters of the string
# (e) The last three characters of the string
# (f) The string backwards
# (g) The seventh character of the string if the string is long enough and a message otherwise
# (h) The string with its first and last characters removed
# (i) The string in all caps
# (j) The string with every a replaced with an e

# prompt the user for a string
string=input("Enter a string: ")

# Print total number of characters
print(len(string));

# print the string 10 times
print(string*10)

# The first character of the string (remember that string indices start at 0)
print(string[0])

# The first three characters of the string
print(string[:3])

# The string backwards
# print(string[])
user_input = input("Please enter a string: ")
print("The string backwards is: " + user_input[::-1])


# The seventh character of the string if the string is long enough and a message otherwise
user_input = input("Please enter a string: ")
if len(user_input) >= 7:
    print("The seventh character of the string is: " + user_input[6])
else:
    print("The string is not long enough.")

    

# The string with its first and last characters removed
print(string[1:-1])

# The string in all caps
print(string.upper())

# The string with every a replaced with an e
original_string = input("Enter a string: ")
modified_string = original_string.replace("a", "e")
print("Modified string: ", modified_string)

    
