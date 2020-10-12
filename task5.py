def my_func_sum_str(text):
    return sum([int(el) for el in text.split()])


number = input("Введите числа через пробел. Для выхода введите q: ")
result = 0
while True:
    if number[-1] != "q":
        result += my_func_sum_str(number)
        print(f"Сумма введенных чисел: {result}")
        number = input("Вы можете продолжить ввод чисел: ")
    else:
        result += my_func_sum_str(number[:-2])
        print(f"Сумма введенных чисел: {result}")
        break
