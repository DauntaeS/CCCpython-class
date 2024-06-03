# convert km to hr or hr to km and return the conversion

speed_type = input("For KM/H to MPH enter: mph otherwise enter kmh ? ").lower()
top_speed = float(input("What was the speed? "))


if speed_type == "kmh":
    # Convert mph to km/h
    kmh = top_speed * 1.60934
    print(f"Your speed was {top_speed} MPH, which is {kmh:.2f} KM/H ")

elif speed_type == "mph":
    # Convert km/h to mph
    mph = top_speed * 0.621371
    print(f"Your speed was {top_speed} KM/H, which is {mph:.2f} MPH")
else:
    print("Invalid input. Please enter 'mph' or 'kmh'.")
