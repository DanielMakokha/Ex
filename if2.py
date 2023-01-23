# Ask the user for a temperature. Then ask them what units, Celsius or Fahrenheit, the temper-
# ature is in. Your program should convert the temperature to the other unit. The conversions
# are F = 95 C + 32 and C = 95 (F − 32).

temperature=float(input("Enter your temp: "));
temp_unit=input("Enter your units: ")
print("Your temp is: ",temperature,temp_unit);

# conditional statement
if temp_unit=="c":
    fahrenheit_temp=(9/5*temperature)+32
    print("Fahrenheit: ",fahrenheit_temp,"f")
if temp_unit=="f":
    celsious_temp=5/9*(temperature-32)
    print("celcious: ",celsious_temp)
