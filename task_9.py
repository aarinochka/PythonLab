tip = input("Выберите тип измерения:\n1.Масса\n2.Длина\n")
if tip == '1':
    from_ed = int(input("Выбрана масса\n1.кг\n2.г\n3.мг\n4.т\n5.ц\nВыберите из какой еединицы: "))
    to_ed = int(input("Выберите в какую еединицу: "))
    value = float(input("введите знаечние: "))
    massa = [1, 10**-3, 10**-6, 10**3, 10**2]
    massa_naz = ["кг", "г", "мг", "т", "ц"]
    result = (value *massa[from_ed-1]/massa[to_ed-1])
    print(f"Результат: {value} {massa_naz[from_ed - 1]} = {result:.3f} {massa_naz[to_ed - 1]}")
elif tip =='2':    
    from_ed = int(input("Выбрана длина\n1.м\n2.см\n3.км\n4.дм\n5.мм\nВыберите из какой еединицы: "))
    to_ed = int(input("Выберите в какую еединицу: "))
    value = float(input("Введите знаечние: "))
    dlina = [1, 10**-2, 10**3, 10**-1, 10**-3]
    result = (value *dlina[from_ed-1]/dlina[to_ed-1])    
    dlina_naz = ["м", "см", "км", "дм", "мм"]
    print(f"Результат: {value} {dlina_naz[from_ed - 1]} = {result:.3f} {dlina_naz[to_ed - 1]}")
else:
    print("Тип измерения выбран неверно")    
