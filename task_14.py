import string
number_list1 = input("Введите 1 список чисел: ")
for i in string.punctuation:
    if(i != '.' and i != '-'):
        number_list1 = number_list1.replace(i,' ')
numbers1 = []    
for i in number_list1.split():
    if i !="" and '.'in i:
        numbers1.append(float(i))
    elif i != "":
         numbers1.append(int(i))

number_list2 = input("Введите 2 список чисел: ")
for i in string.punctuation:
    if(i != '.' and i != ',' and i != '-'):
        number_list2 = number_list2.replace(i,' ')
numbers2 = []    
for i in number_list2.split():
    if i !="" and '.'in i:
        numbers2.append(float(i))
    elif i != "":
         numbers2.append(int(i))
print(f"1 списoк чисел: {numbers1}")      
print(f"2 списoк чисел: {numbers2}")  
print("В обоих:") 
for i in numbers1:
    for j in numbers2:
        if i == j:
            print(i, end = ' ')  
print("\nЕсть в 1, но нет во 2:") 
numbers1no2 = []
for i in numbers1:
    est = False
    for j in numbers2:
        if i == j:
            est = True 
    if not est:
        numbers1no2.append(i)
print(numbers1no2)        
numbers2no1 = []        
print("Есть во 2, но нет в 1:") 
for i in numbers2:
    est = False
    for j in numbers1:
        if i == j:
            est = True 
    if not est:
        numbers2no1.append(i)
print(numbers2no1)
print(f"Только в 1 или только во 2:\n{numbers1no2 + numbers2no1}")        
         