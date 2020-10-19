with open("haiku.txt", encoding='utf-8') as f_obj:
    line = 0
    word_cnt = []
    for el in f_obj:
        line += 1
        word_cnt.append(len(el.split()))

print(f"Количество строк в файле: {line}")
for el in range(line):
    print(f"В строке {el + 1} - {word_cnt[el]} слова")
