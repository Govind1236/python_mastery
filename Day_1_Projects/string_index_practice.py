# animal = "ELEPHANT"
# print(f"The First Letter of animal is: {animal[0]}")
# print(f"The P Letter of animal is: {animal[3]}")
# print(f"The Last Letter of animal is: {animal[7]}")
# print(f"The L Letter of animal is: {animal[1]}")

# String Manupulaion
# phrase = "Python is Powerful and Fun"
# word_is = phrase[7:9]
# print(f"The word is: {word_is}")
# word_powerful = phrase[10:18]
# print(f"The word is: {word_powerful}")

# immutable String
secret_message = "heLLO WORld"
print(f"Original String: {secret_message}")
firs_char_capitialize = secret_message[0].upper()
rest_of_message_lowercase = secret_message[1:].lower()
clear_message = firs_char_capitialize + rest_of_message_lowercase
print(f"Clear Message is: {clear_message}")