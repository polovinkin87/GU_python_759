import json

with open("firm_for_task7.txt", encoding='utf-8') as f_obj:
    line = []
    for el in f_obj:
        el = el.split()
        line.append(el)

result = [{}, {}]
profit_all = []
for el in line:
    profit = int(el[2]) - int(el[3])
    result[0].update({el[0]: profit})
    if profit >= 0:
        profit_all.append(profit)

result[1].update({"average_sale": (sum(profit_all) / len(profit_all))})

with open("profit.json", "w") as f_write:
    json.dump(result, f_write)
