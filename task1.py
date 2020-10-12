def number(var_1, var_2):
    try:
        return f"Результат деления первого числа на второе: {var_1 / var_2}"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"


el_1 = int(input("Введите первое число: "))
el_2 = int(input("Введите второе число: "))
print(number(el_1, el_2))
