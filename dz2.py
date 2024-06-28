import string
from random import randint

password_length = input("Length: ")
password = ""
all_symbols = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]

choice = input(
    "Enter certain type of symbols \n 0 only uppercase letters \n 1 only lowercase letters  \n 2 only digits \n 3 only punctuation \n Choice: ")

if int(choice) == 0 or int(choice) == 1 or int(choice) == 2 or int(choice) == 3:
    for i in range(int(password_length)):
        password += all_symbols[int(choice)][randint(0, len(all_symbols[int(choice)]) - 1)]

    print(password)

else:
    print("Error")
