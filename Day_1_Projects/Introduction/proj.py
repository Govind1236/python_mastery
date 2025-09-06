try:
    num = float(input("Enter a First Number: "))
    num1 = float(input("Enter a Second Number: "))
except ValueError:
    print("Enter a correct numbers")
else:
    choice = input("Enter operators to do the task * + / - .... : ")
    if choice == '+':
        print(f"Addition: {num + num1}")
    elif choice == '-':
     print(f"Subtraction: {num - num1}")
    elif choice == '/':
        print(f"Division: {num / num1}")
    elif choice == '%':
        print(f"Moduls: {num % num1}")
    elif choice == '*':
        print(f"Multiplication: {num * num1}")

