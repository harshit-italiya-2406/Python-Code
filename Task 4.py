t = float(input("Enter the temperature : "))
h = float(input("Enter the Humidity : "))

if t > 40:
        print("Critical temperature")
elif t > 30:
    print("High temperature")
else:
        print("Normal")
if h > 80:
        print("High Humidity")
else:
       print("Normal")