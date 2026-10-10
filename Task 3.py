temperature = int(input("Enter the temperature"))

if temperature < 10:
    print("Very Cold")
elif temperature >= 10 and temperature < 20:
     print("Cold")
elif temperature >= 20 and temperature < 30:
     print("Normal")
elif temperature >= 30 and temperature < 40:
     print("Hot")
else:
     print("Critical")