text = input("Введите предложение из нескольких слов: ")
text = text.split()
i = 1
for el in text:
    print(f"{i}. {el[:10]}")
    i += 1
