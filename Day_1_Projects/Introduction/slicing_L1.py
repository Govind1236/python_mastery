# Input a string s. Print its length, first, and last character (handle empty string).

# Print the 3rd and 2nd-last characters if they exist; otherwise say “Too short”.

# Print s in upper, lower, and title case on three lines.

# Print whether s contains the character 'a' (case-insensitive).

str_ = input("Enter a String: ")
if len(str_) == 0:
    print("Empty String")
else:
    print(f"Lenght: {len(str_)}")
    print(f"First: {str_[0]}")
    print(f"Last: {str_[-1]}")
if len(str_) >= 3:
    print(f"3rd Character: {str_[2]}")
    print(f"2nd Character: {str_[1]}")
else:
    print(f"Too short for 3rd character")

print(f"Upper: {str_.upper()}")
print(f"Lower: {str_.lower()}")
print(f"Title: {str_.title()}")