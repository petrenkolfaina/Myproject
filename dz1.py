import random
num = random.randint(1, 100)
num1 = int(input("Enter your number"))
k = 0
while num1 != num:
    if num1 < num:
        k += 1
        print("Загадкове число більше")
    elif num1 > num:
        k += 1
        print("Загадкове число менше")
    num1 = int(input("Enter your number"))
print("Ви вгадали")
print(k)