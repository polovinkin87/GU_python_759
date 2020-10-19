from random import randint

with open("number_for_task5.txt", "w", encoding='utf-8') as f_obj:
    number = [str(randint(1, 100)) for el in range(10)]
    f_obj.write(" ".join(number))

with open("number_for_task5.txt", encoding='utf-8') as f_obj_n:
    result = f_obj_n.read()
    result = [int(el) for el in result.split()]
    print(f"Сумма чисел в файле: {sum(result)}")
