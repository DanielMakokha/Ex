# Use a for loop to print an upside down triangle like the one below. Allow the user to specify
# how high the triangle should be.

rows=int(input("Enter the number of rows: "))

for i in range(rows,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")