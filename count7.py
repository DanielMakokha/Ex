# Write a program that swaps the values of three variables x , y , and z , so that x gets the value
# of y , y gets the value of z , and z gets the value of x .

"""# Initialize the variables x, y, and z
x = 1
y = 2
z = 3

# Use a temporary variable to store the value of x
temp = x

# Assign the value of y to x
x = y

# Assign the value of z to y
y = z

# Assign the value of the temporary variable to z
z = temp

# Print the new values of x, y, and z
print("x:", x)
print("y:", y)
print("z:", z)"""

# initialize variables
x=1
y=2
z=3

x,y,z=y,z,x
print("x: ",x)
print("y: ",y)
print("z: ",z)

