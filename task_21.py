import time
def timing(func):
    def wrapper(*args):
        start = time.perf_counter()
        func(*args)
        end = time.perf_counter()
        print(f"{func.__name__}{args} выполняется {(end-start)*1000} мс")
        return func(*args)
    return wrapper
        
@timing
def add_dict (dict, key, list):
    dict[key] = list

@timing
def summa(a,b,c,d):
    return a+b+c+d

@timing
def stroki(str1, str2):
    return str1 + str2

@timing
def append_list(list, a, b):
    list.append(a)
    list.append(b)

@timing
def print_hi():
    return "hi"

dict_a = {"a" : 1, "b" : {"c" : 1, "f" : 4}}
summa(1,2,3,4)   
append_list([1,2,3,4],5,6)
summa(1.5,2.3,7,8)
stroki("при", "вет")
stroki("aaa","bbb")
add_dict(dict_a, "e", [1,2,3])
add_dict(dict_a, "a", (1,2,3,4))
print_hi()