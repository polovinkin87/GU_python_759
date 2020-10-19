number_k = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}

with open("number.txt", encoding='utf-8') as f_obj:
    number_l = {}
    for el in f_obj:
        el = el.split("-")
        number_l.update({int(el[1]): (el[0])})

with open("number_new.txt", "w", encoding='utf-8') as f_obj_n:
    for el_1 in number_l.keys():
        for el_2 in number_k.keys():
            if el_1 == el_2:
                f_obj_n.write(f"{number_k[el_2]}-{el_2}\n")
                break
