import time
def loq_calls(filename):
    def decorator(func):
        def wrapper(*args):
            now = time.ctime()
            with open(filename, "a") as file:
                file.write(f"{now}: {func.__name__}{args}\n")
            return func(*args)
        return wrapper
    return decorator


open("task_18.txt", "w").close()
@loq_calls("task_18.txt")
def add_dict (dict, key, list):
    dict[key] = list

@loq_calls("task_18.txt")
def summa(a,b,c,d):
    return a+b+c+d

@loq_calls("task_18.txt")
def stroki(str1, str2):
    return str1 + str2

@loq_calls("task_18.txt")
def append_list(list, a, b):
    list.append(a)
    list.append(b)

@loq_calls("task_18.txt")
def print_hi():
    print("hi")


dict_a = {"a" : 1, "b" : {"c" : 1, "f" : 4}}
summa(1,2,3,4)   
append_list([1,2,3,4],5,6)
summa(1.5,2.3,7,8)
stroki("при", "вет")
stroki("aaa","bbb")
add_dict(dict_a, "e", [1,2,3])
add_dict(dict_a, "a", (1,2,3,4))
print_hi()

