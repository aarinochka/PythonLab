import string
number_list = input("Введите список чисел: ")
for i in string.punctuation:
    if(i != '.' and i != '-'):
        number_list = number_list.replace(i,' ')
numbers = []    
for i in number_list.split():
    if i !="" and '.'in i:
        numbers.append(float(i))
    elif i != "":
         numbers.append(int(i))
print(f"Списрк чисел: {numbers}")       
number_count = {}
for i in numbers:
    if i in number_count:
        number_count[i] += 1
    else:
        number_count[i] = 1   
print("Уникальные: ")
for i in number_count:
    if number_count[i] == 1:
        print(i, end=' ')
print("\nПовторяющиеся: ")
for i in number_count:
    if number_count[i] > 1:
        print(i, end=' ')
print("\nЧетные: ")
for i in number_count:
    if int(i) % 2 == 0:
        print(i, end=' ')    
print("\nНечетные: ")
for i in number_count:
    if int(i) % 2 == 1:
        print(i, end=' ')   
print("\nОтрицательны: ")
for i in number_count:
    if i < 0:
        print(i, end=' ')  
print("\nС плавающей точкой: ")
for i in number_count:
    if  type(i) == float:
        print(i, end=' ')                          
sum5 = 0
for i in number_count:
    if i % 5 == 0:
        sum5 += i
print(f"\nСумма, кратных 5: {sum5}")  
max_number = numbers[0]
min_number = numbers[0]
for i in number_count:
    if max_number < i:
        max_number = i
    if min_number > i:
        min_number = i
print(f"Самое большое: {max_number}\nСамое маленькое: {min_number}")        