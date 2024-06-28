import random
num = random.randint(1, 100)
num1 = int(input("Enter your number"))
while num1 != num:
    if num1 < num:
        print("Загадкове число більше")
    elif num1 > num:
        print("Загадкове число менше")
    num1 = int(input("Enter your number"))
print("Ви вгадали")
