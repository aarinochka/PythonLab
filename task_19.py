def cache(func):
    cache_dict = {}
    def wrapper(*args):
        key = str(args)
        if key in cache_dict:
            print(f"Возвращаем из кэша функции {func.__name__} для {key}")
            return cache_dict[key]    
        print(f"Вычисляем {func.__name__} для {key}")
        cache_dict[key] = func(*args)
        return func(*args)
    return wrapper

@cache
def add(a,b,c):
    return a+b+c

@cache 
def in_dict(dict, key1):
   if key1 in dict:
       return True
   else:
       return False

add(1,2,3)
add(4,5,6)
add(1,2,4)  
add(1,2,3)  
add(1,2,4)  
add(4,5,7)

dict_d = {"a" : [1,3], "b" : {"A" : 100}, "c" : {"D" : 40, "C" : 100}, "e" : (3,4)  }     
in_dict(dict_d, "a")
in_dict(dict_d, 'b')
in_dict(dict_d, 'v')
in_dict(dict_d, 'a')
in_dict(dict_d, 'v')
in_dict(dict_d, 'm')

    
    