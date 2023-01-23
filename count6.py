# Write a program that finds all four of the perfect numbers
# that are less than 10000.

# Initialize a variable to store the sum of divisors
divisor_sum = 0

# Initialize a counter for the number of perfect numbers found
perfect_numbers_count = 0

# Iterate through the numbers from 1 to 10000
for n in range(1, 10000):
    divisor_sum = 0
    # Iterate through the numbers from 1 to n/2
    for i in range(1, n//2+1):
        # Check if the current number is a divisor
        if n % i == 0:
            # If the current number is a divisor, add it to the sum
            divisor_sum += i
    # Check if the current number is a perfect number
    if divisor_sum == n:
        # If the current number is a perfect number, print it and increment the counter
        print(n)
        perfect_numbers_count += 1

print("Number of perfect numbers found:", perfect_numbers_count)
