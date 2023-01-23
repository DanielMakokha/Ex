# Write a program that counts how many of the squares of the numbers from 1 to 100 end in a
# 4 and how many end in a 9.

"""
count4=0;
count9=0;

for i in range(1,100):
    if i**2%10==4:
        count4=count4+1
    elif i**2%10==9:
        count9=count9+1
print(count4)      
print(count9)
"""
# Initialize counters for squares ending in 4 and 9
squares_ending_in_4 = 0
squares_ending_in_9 = 0

# Iterate through the numbers from 1 to 100
for i in range(1, 101):
    # Calculate the square of the current number
    square = i**2
    # Check the last digit using modulus operator
    if square % 10 == 4:
        squares_ending_in_4 += 1
    elif square % 10 == 9:
        squares_ending_in_9 += 1

# Print the results
print("Squares ending in 4:", squares_ending_in_4)
print("Squares ending in 9:", squares_ending_in_9)
