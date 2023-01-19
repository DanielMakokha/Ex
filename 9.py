while True:
    try:
        hour = int(input("Enter an hour between 1 and 12: "))
        if hour < 1 or hour > 12:
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 12.")

future_hours = int(input("Enter how many hours in the future you want to go: "))

future_hour = (hour + future_hours) % 12
if future_hour == 0:
    future_hour = 12

print("The hour will be: ", future_hour)
