# Get user input
width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))

# Initialize counter
counter = 0

# Draw rectangle
for i in range(height):
    for j in range(width):
        print(counter % 10, end=' ')
        counter += 1
    print()
