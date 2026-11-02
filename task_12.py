import string
text = input("Введите текст: ")
text = text.lower()
for i in string.punctuation:
    text = text.replace(i,' ')
words = []    
for i in text.split():
    if i !="":
        words.append(i)
print(f"Отдельные слова: {words}")
print(f"Кол-во слов: {len(words)}")
word_count = {}
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i]  = 1
print("Кол-во каждого слова:")
for i in word_count:
    print(f"{i} - {word_count[i]}") 

print(f"Самые частые слова:")   
max_count = 0 
for i in word_count:
    if word_count[i] > max_count:
        max_count = word_count[i]
for i in word_count:
    if max_count == word_count[i]:       
        print(f"{i} - {word_count[i]}") 
        
max_len = len(words[0])
min_len = len(words[0])
for i in word_count:
    if len(i) < min_len:
        min_len = len(i)
    if len(i) > max_len:
        max_len = len(i)
print("Самые короткие:")
for i in word_count:
    if len(i) == min_len:
        print(f"{i} ({min_len})")
print("Самые длинные:")
for i in word_count:
    if len(i) == max_len:
        print(f"{i} ({max_len})")       



long_words = []
for i in words:
    if len(i) >= 3:
        long_words.append(i)
print(f"\nОтдельные слова: {long_words}")

print(f"Кол-во слов: {len(long_words)}")
word_count = {}
for i in long_words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i]  = 1
print("Кол-во каждого слова:")
for i in word_count:
    print(f"{i} - {word_count[i]}") 

print(f"Самые частые слова:")   
max_count = 0 
for i in word_count:
    if word_count[i] > max_count:
        max_count = word_count[i]
for i in word_count:
    if max_count == word_count[i]:       
        print(f"{i} - {word_count[i]}") 
        
max_len = len(long_words[0])
min_len = len(long_words[0])
for i in word_count:
    if len(i) < min_len:
        min_len = len(i)
    if len(i) > max_len:
        max_len = len(i)
print("Самые короткие:")
for i in word_count:
    if len(i) == min_len:
        print(f"{i} ({min_len})")
print("Самые длинные:")
for i in word_count:
    if len(i) == max_len:
        print(f"{i} ({max_len})")       
