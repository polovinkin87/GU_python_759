with open("firm.txt", encoding='utf-8') as f_obj:
    line = []
    for el in f_obj:
        el = el.split()
        line.append(el)

result = {}
for el_1 in line:
    num_el = 0
    for el_2 in el_1[1:]:
        number = ""
        for el_3 in range(len(el_2)):
            if el_2[el_3].isdigit():
                number += el_2[el_3]
        try:
            num_el += int(number)
        except ValueError:
            num_el
    result.update({el_1[0]: num_el})

print(result)
