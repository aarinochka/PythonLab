text = input("Введите строку: ")
text1 = text.lower().replace(" ","")
revers_text = text1[::-1]
if text1 == revers_text:
    print(f"Строка {text} является полидромом")
else:
    print(f"Строка {text} НЕ является полидромом")

        
