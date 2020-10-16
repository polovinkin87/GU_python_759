from sys import argv


def salary(agr_1, arg_2, arg_3):
    return int(agr_1) * int(arg_2) + int(arg_3)


script_name, work_in_hour, sale_hour, prize = argv

print("Выработка в часах: ", work_in_hour)
print("Ставка в час: ", sale_hour)
print("Премия: ", prize)
print(f"Заработная плата: {salary(work_in_hour, sale_hour, prize)}")
