age = int(input("Введите возраст: "))
zp = int(input("Введите ежемесячный доход: "))
kredit = int(input("Введите размер запрашиваемого кредита: "))
srok = int(input("Введите срок кредита в месяцах: "))
kred_ist = input("Выберите тип вашей кредитной истории: 1.отличная 2.хорошая 3.удовлетворительная 4.плохая ")
porych = bool(input("Если у вас есть поручитель, то введите 1, если нет, то Enter "))
zalog = bool(input("Если у вас есть залог, то введите 1, если нет, то Enter "))
kr_k_zp = kredit/srok/zp
print(f"\nСоотношенияе кредита к доходу: {int(kr_k_zp*100)} %")
if (kr_k_zp < 0.3) and (kred_ist == '1' or kred_ist == '2') and porych and zalog and (25 <= age <= 45):
    print("Категория риска: низкая")
    risk = 1
elif (kr_k_zp < 0.5) and (kred_ist != '1') and (porych or zalog) and (18 <= age <= 60):
    print("Категория риска: средняя")
    risk = 2
elif (kr_k_zp < 0/7) and (kred_ist != '1') and (18 <= age <= 60) :
    print("Категория риска: высокая")
    risk = 3
else:
    print("Категория риска: критическая")
    risk = 4
prozent = 15
if risk == 1:
    prozent-=2
if risk ==4:
    prozent+=5
if zalog:
    prozent-=2
if porych:
    prozent-=1
if 25 <= age <= 45:
    prozent-=1
if age > 60:
    prozent+=2
if prozent < 10:
    prozent = 10    
print(f"Рекомендуемая процентная ставка: {prozent} %")
if risk ==1 or risk ==2 or (risk == 3 and (zalog or porych) or (risk == 4 and zalog and porych and (18 <= age <= 60))):
    print("Рекомендация: Одобрить")
else:
    print("Рекомендация: Отклонить")