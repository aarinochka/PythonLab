def merge_dicts(dict_1, dict_2):
    for key2 in dict_2.keys():
        if key2 in dict_1.keys():
            if type(dict_1[key2]) == dict and type(dict_2[key2]) == dict:
                merge_dicts(dict_1[key2], dict_2[key2])
            else:
                dict_1[key2] = dict_2[key2]
        else:
            dict_1[key2] = dict_2[key2]
    return dict_1        


     

dict_a = {"a" : 1, "b" : {"c" : 1, "f" : 4}}
dict_b = {"d" : 1, "b" : {"c" : 2, "e" : 3}}
print(f"Исходные словари:\n{dict_a}\n{dict_b}")
print(f"После слияния:\n{merge_dicts(dict_a, dict_b)}\n")

dict_c = {"a" : [2,4,5], "b" : 2, "c" : {"A" : 10, "B" : 20, "C" : {"l" : [10,20]}}, "d" : (1,2)}        
dict_d = {"a" : [1,3], "b" : {"A" : 100}, "c" : {"D" : 40, "C" : 100}, "e" : (3,4)  }     
print(f"Исходные словари:\n{dict_c}\n{dict_d}")
print(f"После слияния:\n{merge_dicts(dict_c, dict_d)}")           