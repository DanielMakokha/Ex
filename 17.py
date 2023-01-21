# A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
# unless they are also divisible by 400. Ask the user to enter a year, and, using the // operator,
# determine how many leap years there have been between 1600 and that year.

# Enter input from the user.

# Get user input
year = int(input("Enter a year: "))

# Initialize count of leap years
leap_years = 0

# Loop through years from 1600 to the input year
for i in range(1600, year + 1):
    # Check if the year is a leap year
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        leap_years += 1

# Print the result
print("Number of leap years between 1600 and", year, ":", leap_years)
