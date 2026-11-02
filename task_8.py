import random
number = random.randint(0,100)
num = int(input("Введите число: "))
while num != number:
    print("Меньше") if num > number else print("Больше")
    num = int(input("Введите число: "))
print(f"Вы угадали! Это число {number}")    
