checklist = []
print("Введите последовательно несколько элементов. Для выхода нажмите q")
i = 1
while True:
    el = input(f"Элемент {i}: ")
    if el != 'q':
        checklist.append(el)
    else:
        break
    i += 1

print(f"Исходный список {checklist}")

for el in range(1, len(checklist), 2):
    checklist[el-1], checklist[el] = checklist[el], checklist[el-1]

print(f"Форматированный список {checklist}")
