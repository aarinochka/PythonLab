import math
def print_cat(dict_rd):
    i = 1
    for key in dict_rd:
        print(f"{i}. {key}")
        i+=1

def add_remove_category(dict_rd):
    while True:
        print("Категории: ")
        print_cat(dict_rd)
        add_cat = input("Введите 1, если желаете ДОБАВИТЬ категорию, и Enter, если нет: ")
        if add_cat:
            new_cat = input("Введите название категории: ")
            if new_cat and new_cat not in dict_rd:
                dict_rd[new_cat] = 0
                print(f"Категория '{new_cat}' добавлена")
            else:
                print("Такая категория уже есть или вы не ввели название категории")
        else:
            break
    while True:
            print("Категории: ")
            print_cat(dict_rd)
            remove_cat = input("Введите 1, если желаете УДАЛИТЬ категорию, и Enter, если нет: ")
            if remove_cat:
                delete_cat = input("Введите название категории, которую хотите удалить: ")
                if delete_cat and delete_cat in dict_rd:
                    del dict_rd[delete_cat]
                    print(f"Категория '{delete_cat}' удалена")
                else:
                    print("Такой категории нет или вы не ввели название категории")
            else:
                break    
def vvod_summ(str, dict_rd):
    print(f"Введите {str}:")
    for key in dict_rd :
        dict_rd[key] = int(input(f"{key}: "))   

print("Доходы: ")
dict_doxodov = {"зп" : 0, "подработки" : 0, "прочие" : 0}
add_remove_category(dict_doxodov)
vvod_summ("доходы", dict_doxodov)
print("Расходы:")
dict_rasxod = {"жилье" : 0, "транспорт" : 0, "питание" : 0, "развлечения" : 0, "здоровье" : 0, "учеба" : 0, "прочие" : 0}
add_remove_category(dict_rasxod)
vvod_summ("расходы", dict_rasxod)
doxod = sum(dict_doxodov.values())
rasxod = sum(dict_rasxod.values())
ostatok = doxod - rasxod
print(f"Ваш общий доход: {doxod} руб\nВаш общий расход: {rasxod} руб\nОстаток: {ostatok} руб")
procent_ostatok = math.ceil(ostatok/doxod)
if ostatok >= doxod*0.2:

    print(f"Ежемесечно вы откладываете {procent_ostatok} % от дохода. Это хороший показатель")
elif ostatok > 0:
        print(f"Вы откадываете недостаточно, старайтесь откладывать хотя бы {doxod*0.2} руб")
elif ostatok == 0:
        print(f"Ваши доходы равны расходам, постарайтесь уменьшить расходы, чтобы вы могли откладывать хотя бы {doxod*0.2} руб")
else:
     print(f"Вы тратите больше, чем зарабатывайте, срочно пересмотрите свои доходы и расходы. В идеале вы должны откладывать {doxod*0.2} руб")


max_rasxod = 0
list_max_rasxod = []
for value in dict_rasxod.values():
     if value > max_rasxod:
          max_rasxod = value
for key, value in dict_rasxod.items():
     if value == max_rasxod:
          list_max_rasxod.append(key)
if len(list_max_rasxod) == 1:          
    print(f"Вы больше всего тратите на категорию {list_max_rasxod[0]}: {max_rasxod} руб\nЭто составляется {math.ceil(max_rasxod*100/doxod)}% от вашего дохода")                   
else:
    print("Больше всего вы тратите на категории:")
    for i in range(len(list_max_rasxod)):
          print(f"{i+1}. {list_max_rasxod[i]}")
    print(f"Вы тратите на каждую из них {max_rasxod} руб\nЭто составляется {math.ceil(max_rasxod*100/doxod)}% от вашего дохода ")      


limits = {"жилье" : 30, "транспорт" : 15, "питание" : 25, "развлечения" : 20, "здоровье" : 20, "учеба" : 10}
for cat, limit in limits.items():
     if cat in dict_rasxod :
          procent = math.ceil(dict_rasxod[cat]*100/doxod)
          if procent >= limit:
            print(f"Вы тратите на {cat} слишком много: {dict_rasxod[cat]} руб ({procent}%)\nСоветую пересмотреть эту категорию")


big_purchase = input("Введите 1, если вы планируете крупную покупку в ближайшее время, и Enter, если нет: ")
if big_purchase:
    if ostatok <= 0:
        print("Вы тратите больше, чем зарабатываете. Для начала наладьте ваши доходы и расходы, а потом планируйте крупные покупки")
    else:       
        summ_big_pur = int(input("Введите сумму этой покупки: "))    
        time_big_pur = int(input("Через сколько месяцев вы хотите ее купить? (нажмите Enter, если прями сейчас): "))
        if time_big_pur:
            if summ_big_pur > ostatok:
                month_big_pur = math.ceil((summ_big_pur - ostatok)/time_big_pur)
                print(f"Вам надо отложить {ostatok}руб, заработанные за этот месяц, и откладывать по {month_big_pur} руб следующие {time_big_pur} месяцев")
                min_month_big_pur = math.ceil(summ_big_pur/ostatok - 1)
                print(f"или\nВы можете купить через {min_month_big_pur} месяцев, откладывая как в этом по {ostatok} руб")
            else:
                if summ_big_pur < ostatok:
                    print("Вы можете совершить эту покупку прямо сейчай")
                else:
                    print(f"Вы не можете совершить эту покупку прямо сейчас, вам не хватает еще {summ_big_pur - ostatok} руб")
                    print(f"Вы сможете накопить это примерно за {math.ceil((summ_big_pur- ostatok)/ostatok)} месяцев")


