def sale(func):
    def warpper(*args):
        summa = func(*args)
        with open('task_24.txt', "a") as f:
            f.write(f"Общая сумма: {summa} руб\n")
        if summa > 100:
            with open('task_24.txt', "a") as f:
                f.write(f"Скидка: -{summa*0.1:.1f} руб\n ")
            return summa*0.9
        else:
            with open('task_24.txt', "a") as f:
                f.write(f"Скидка: 0 руб\n ")
            return summa
    return  warpper  

open('task_24.txt', "w").close()          

tovar = []
kolvo = []
price = []
print("Список товаров:")
while True:
    name = input("Введите название товара, если ввели все товара, то нажмите Enter: ")
    if name:
        tovar.append(name)
        kolvo.append(int(input("Кол-во: ")))
        price.append(int(input("Цена: ")))
    else:
        break
    
@sale
def summ(tovar_,kolvo_, price_):
    summa = 0
    for i in range(len(kolvo)):
        summa += kolvo[i]*price[i]
    with open('task_24.txt', "a") as f:
        f.write("Все товары:\n")
    for i in range(len(kolvo)):
        with open('task_24.txt', "a") as f:
            f.write(f"{tovar[i]}: {price[i]} х {kolvo[i]} = {price[i]*kolvo[i]} руб\n")
    return summa

with open('task_24.txt', "a") as f:
     f.write(f"Итоговая сумма: {summ(tovar,kolvo,price):.1f} руб")




