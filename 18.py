# Get user input
change = float(input("Enter an amount of change less than $1.00: "))

# Convert to cents
cents = int(change * 100)

# Calculate number of quarters
quarters = cents // 25
cents = cents % 25

# Calculate number of dimes
dimes = cents // 10
cents = cents % 10

# Calculate number of nickels
nickels = cents // 5
cents = cents % 5

# Calculate number of pennies
pennies = cents

# Print results
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
