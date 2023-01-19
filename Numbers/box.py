height=int(input("Enter the height: "));
widht=int(input("Enter the widhth: "));

print("The height of the box is ",height,"and the width is ",widht);

for i in range(0,height):
    for j in range(0,widht):
        if(i==0 or i==height-1 or j==0 or j==widht-1):
            print("*",end=" ")
        else:
            print(" ",end=" ");
    
    print()