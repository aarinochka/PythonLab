def plosk_list(no_plosk_list):
    plosk = True
    for i in no_plosk_list:
        if type(i)== list:
            plosk = False
            for j in i:
                if j != []:
                    no_plosk_list.insert(no_plosk_list.index(i),j)
            no_plosk_list.remove(i)
    if  not plosk:
        plosk_list(no_plosk_list)
    return no_plosk_list

list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]     
print("Исходный список: ", list_a)  
print(f"Плоский список: {plosk_list(list_a)}")

list_b = [1,[], [2], [2, [2, [2], [5], [6, [9], 0], [4,[4,[4,[4,[], [9], 6], 0, [12], 0, 8], [9]]]]]]
print("Исходный список: ", list_b)  
print(f"Плоский список: {plosk_list(list_b)}")