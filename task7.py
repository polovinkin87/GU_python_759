def fact(number):
    result = 1
    for element in range(1, number + 1):
        result *= element
        yield result


for el in fact(7):
    print(el)
