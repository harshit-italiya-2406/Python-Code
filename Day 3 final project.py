for i in range (5):
    print("\n Sensor Reading", i+1)

    temperature = float(input("Enter Temperature : "))
    humidity = float(input("Enter Humidity : "))
    if temperature > 40:
        print("Critical")
    elif temperature> 30 :
        print ("High")
    elif temperature< 10 :
        print("Low")
    else: 
        print("Normal")
    if humidity > 80 :
        print("Humidity High")
    else:
        print("Humidity Normal")

        print ("---------------------")
