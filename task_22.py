def type_check(*types):
    def decorator(func):
        def wrapper(*args):
            for i in range(len(args)):
                if type(args[i]) != types[i]:
                    raise TypeError(f"'{args[i]}' имеет тип {type(args[i]).__name__}, а должен быть {types[i].__name__}") 
            print(f"В {func.__name__}{args} все ок")
            return func(*args)
        return wrapper
    return decorator

@type_check(dict, str,list)
def add_dict (dict, key, list):
    dict[key] = list

@type_check(int, int, int, int)
def summa(a,b,c,d):
    return a+b+c+d

@type_check(str, str)
def stroki(str1, str2):
    return str1 + str2

@type_check(list, int, int)
def append_list(list, a, b):
    list.append(a)
    list.append(b)


dict_a = {"a" : 1, "b" : {"c" : 1, "f" : 4}}
add_dict(dict_a, "e", [1,2,3])
summa(1,2,3,4)   
stroki("при", "вет")
append_list([1,2,3,4],5,6)

add_dict(dict_a, 1 , (1,2,3,4))

