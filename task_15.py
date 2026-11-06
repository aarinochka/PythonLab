products = []
print("Введите данные о товарах. Для окончания введите '!': ")
name = input("Название: ")
while name != '!':
    price = float(input("Цена: "))
    kolvo = int(input("Кол-во: "))
    product = {"name": name, "price" : price, "kolvo" : kolvo}
    products.append(product)
    name = input("Название: ")
print(f"Список товаров:\n {products}")
profit={}
for i in products:
    if i["name"] in profit:
        profit[i["name"]] += i["price"] * i["kolvo"]
    else:
        profit[i["name"]] = i["price"] * i["kolvo"]
print(f"Прибыль с каждого товара:\n {profit}")  
max_profit = 0
for key in profit.keys():
    if max_profit < profit[key]:
        max_profit = profit[key] 
print("Самые прибыльные:")
for key in profit.keys():
    if max_profit == profit[key]:      
        print(f"{key} - {profit[key]}")   
print(f"Кол-во уникальных: {len(profit)}")                  
