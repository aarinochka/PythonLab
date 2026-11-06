from datetime import date
price = float(input("Введите сумму покупки: "))
day = int(input("Введите день вашего рождения: "))
month = int(input("Введите номер месяца вашего рождения: "))
year = int(input("Введите год вашего рождения: "))
vip = bool(input("Если Вы vip введите любой символ, если нет, то нажмите Enter: "))
sale = 0
if vip:
    sale += 15
elif price > 1000:
    sale += 10 
today = date.today()
if day == today.day and month == today.month:
    sale += 5 
age = today.year - year 
if(month, day) < (today.month, today.day):
    age -= 1
if age > 63:
    sale += 5 
print(f"Ваша скидка составила: {sale} %")