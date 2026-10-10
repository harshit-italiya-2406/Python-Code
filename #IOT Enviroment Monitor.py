#IOT Enviroment Monitor

t = float(input("Enter temperature : "))
h = float(input("Enter Humidity : "))
print(t,"°C")
print(h, "%")

if t > 40: 
   print("CRITICAL TEMPERATURE")

elif t > 30:
     print("HIGH TEMPERATURE")
elif t < 10:
    print("Wear Jacket because temperature is low")
    
else: 
    print("TEMPERATURE NORMAL")

if h > 80:
   print ("HIGH HUMIDITY")

else:
    print("HUMIDITY NORMAL")