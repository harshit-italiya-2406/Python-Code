correct_username = "admin"
correct_password = 1234

username = input("Enter your username : ")
password = int(input("Enter Your password : "))

if username == correct_username and password == correct_password:
    print("Login successfull")
else: print("Incorect username or password") 