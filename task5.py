rev = int(input("Введите значение выручки фирмы: "))
cost = int(input("Введите значение издержек фирмы: "))

if rev > cost:
    print("Фирма работает в прибыль")
    profit = (rev - cost) / rev
    print(f"Рентабельность выручки: {int(profit * 100)}%")
    cnt_people = int(input("Введите количество сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного человека: {int((rev - cost) / cnt_people)}")
else:
    print("Фирма работает в убыток")
