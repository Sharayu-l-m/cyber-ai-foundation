username = input("Enter username: ").strip().lower()
password = input("Enter password: ").strip()

if username == "admin" and password == "1234":
    print("Login successful ")
elif username == "admin":
    print("Wrong password ")
else:
    print("User not found ")
