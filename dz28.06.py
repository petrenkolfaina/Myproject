import random
import string

user_len = int(input("Enter a len:"))
symbols_choice = input("Enter type of the symbols:\n 0 only punctuation \n 1  only uppercase letters \n 2  only lowercase letters \n 3 only digits \n Choice:")
Punctuation = string.punctuation
Uppercase = string.ascii_uppercase
Lowercase = string.ascii_lowercase
Digits = string.digits
symbols = ""

if symbols_choice == "0":
    symbols = Punctuation
elif symbols_choice == "1":
    symbols = Uppercase
elif symbols_choice == "2":
    symbols = Lowercase
elif symbols_choice == "3":
    symbols = Digits
else:
    print("Error")

password = "".join(random.choice(symbols) for i in range(user_len))
print(password)
