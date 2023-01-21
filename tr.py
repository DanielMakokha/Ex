#  Use a for loop to print a triangle like the one below. Allow the user to specify how high the
# triangle should be.

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ",end=" ")
    print("\n")