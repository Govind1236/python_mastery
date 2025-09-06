# check = int(input("Enter a number: "))
# if check % 2 == 0 :
#     print("Its Even")
# else:
#     print("Its Odd")

try:
    value = int(input("Enter a Number: "))
except ValueError:
    print("Enter value is not numbers")
else:
    if value > 0:
         print("Positive")
    elif value < 0:
        print("Negative")
    else:
      print("Zero")
