print("Welcome to Day 13 Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "5":
        print("Exiting Calculator. Bye!")
        break

    if choice in ["1","2","3","4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Error: Cannot divide by 0")
    else:
        print("Invalid Input. Try again.")
        
        
