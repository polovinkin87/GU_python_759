with open("company.txt", encoding='utf-8') as f_obj:
    firm = {}
    for el in f_obj:
        el = el.split()
        firm.update({el[0]: el[1]})

fio = [el for el in firm.keys() if int(firm[el]) < 20000]
salary = [int(el) for el in firm.values()]

#print(firm)
print(f"Сотрудники фирмы имеющие оклад менее 20 тыс.: {', '.join(fio)}")
print(f"Средний оклад сотрудников фирмы: {'%.2f'%(sum(salary) / len(salary))}")
