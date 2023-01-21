# Question 13
# # A programs that asks user to enter a number and prints the Sine,cos & tan of that number
# 
# import math
# from math import sin,cos,tan
# num=int(input("Enter a number: "));
# print("Sine: ",sin(num))
# print("Cosine: ",cos(num))
# print("tangent: ",tan(num))



import math

# Ask the user for a number
num = float(input("Enter a number: "))

# Calculate sine, cosine, and tangent
sin = math.sin(num)
cos = math.cos(num)
tan = math.tan(num)

# Print the results
print("Sine: ", sin)
print("Cosine: ", cos)
print("Tangent: ", tan)
