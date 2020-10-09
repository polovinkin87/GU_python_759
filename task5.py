my_list = [13, 7, 5, 3, 3, 2]
number = int(input("Введите натуральное число: "))

for el in range(len(my_list)):
    if number > my_list[el]:
        my_list.insert(el, number)
        break
    elif el == len(my_list)-1:
        my_list.append(number)

print(my_list)
