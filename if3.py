# Ask the user to enter a temperature in Celsius. The program should print a message based
# on the temperature:
# • If the temperature is less than -273.15, print that the temperature is invalid because it is
# below absolute zero.
# • If it is exactly -273.15, print that the temperature is absolute 0.
# • If the temperature is between -273.15 and 0, print that the temperature is below freezing.
# • If it is 0, print that the temperature is at the freezing point.
# • If it is between 0 and 100, print that the temperature is in the normal range.
# • If it is 100, print that the temperature is at the boiling point.
# • If it is above 100, print that the temperature is above the boiling point.

temp_celc=float(input("Enter temperature in celcious: "));

if temp_celc < -273.15:
    print(temp_celc,"is invalid");
elif temp_celc==-273.15:
    print(temp_celc,"is absolute 0")
elif temp_celc<=0:
    print(temp_celc,"is below freezing point");
elif temp_celc==0:
    print(temp_celc,"is at freezing point");
elif temp_celc<=100:
    print(temp_celc,"is in the normal range");
elif temp_celc==100:
    print(temp_celc,"temp is at boiling point");
else:
    print(temp_celc,"is above boiling point")