# Print numbers 1 to 5 using range.
'''
----range-----
a = 5
for i in range(1, a):
    print(i)'''

# Print even numbers 2 to 20 (use step).
# for i in range(20, 0, -1):
#     print(f"Decending Numbers: {i}")
try:
    n = int(input("Enter a number: "))
    if n < 0:
           print(f"Please Enter a postive number ")
    else:
          for i in range(1, n + 1):
            print(i)
except ValueError:
    print("Enter a Valid Integer ")
