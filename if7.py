# Write a program that asks the user for two numbers and prints Close if the numbers are
# within .001 of each other and Not close otherwise.

a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
diff=a-b;
if diff <=0.001:
    print("Close");
else:
    print("Not Close");