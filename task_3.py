amount = int(input("Введите сумму в рублях: "))
nominals = [100, 50, 10, 5, 2, 1]
print(f"Размен {amount} рублей:")
for i in nominals:
    count = amount // i
    amount %= i
    if count > 0:
        print(f"{count} по {i} руб")




