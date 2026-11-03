def unik_elements(no_plosk_list):
    plosk = True
    for i in no_plosk_list:
        if type(i)== list:
            plosk = False
            for j in i:
                if j != []:
                    no_plosk_list.insert(no_plosk_list.index(i),j)
            no_plosk_list.remove(i)
    if  not plosk:
        unik_elements(no_plosk_list)
    count_el = {}
    for i in no_plosk_list:
        if i in count_el.keys():
            count_el[i] +=1
        else:
            count_el[i] = 1
    unik_el = []        
    for i in  count_el.keys():
        if(count_el[i] == 1):
            unik_el.append(i)
    return unik_el

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]     
print("Исходный список: ", list_a)  
print(f"Уникальные элементы: {unik_elements(list_a)}")

list_b = [1,[], [2], [2, [2, [2], [5], [6, [7], 7], [8,[4,[4,[4,[], [9], 9], 0, [12], 0, 8], [9]]]]]]
print("Исходный список: ", list_b)  
print(f"Уникальные элементы: {unik_elements(list_b)}")