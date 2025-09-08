start = int(input("Enter a start number: "))
stop = int(input("Enter a stop number: "))

skip = int(input("Enter a number to be skip: "))
if start > stop:
    print("Enter less number in start")  
elif skip not in range(start, stop + 1):
          print("Skip Is out of range: ")
else:
      for i in range(start, stop + 1):
        if i == skip:
            continue
        print(i)
