baz_price = 24.99
nalog = 0
dop_price = 0
max = [60, 30, 1000]
one_price = [0.89, 0.59, 0.79]
dop_price_servise = [0,0,0]
min = int(input("Введите кол-во израсходаванных минут: ")) 
sms = int(input("Введите кол-во отправленных смс: "))
internet = int(input("Введите кол-во потраченных Мб: "))
print(f"Базовая сумма: {baz_price} руб")
vyvod = ["Сумма за доп. минуты: ", "Сумма за доп. смс: ", "Сумма за доп. интеренет: "]
servise = [min, sms, internet]
for i  in range(0,3):
    if servise[i] > max[i]:
        dop_price_servise[i] += one_price[i]*(servise[i]-max[i])
        print(f"{vyvod[i]} {dop_price_servise[i]} руб")
        dop_price += dop_price_servise[i]
print(f"Налог: {dop_price*0.02:.2f} руб")    
print(f"Итоговая сумма: {baz_price+ dop_price*1.02:.2f} руб")    
