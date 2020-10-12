def int_func(word):
    return word.capitalize()


text = input("Введите несколько слов: ")
result = map(int_func, text.split())
print(" ".join(result))
