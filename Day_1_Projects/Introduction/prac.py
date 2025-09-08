# string = input("Enter a String: ")
# index = int(input("Enter a Number: "))
# if 0 <= index < len(string):
#     print(string[index])
# else:
#     print("Out of Range")

password = input("Enter A Password: ")
if len(password) <= 5:
    print("Password length should at least 6")
else:
    print("login Successful")