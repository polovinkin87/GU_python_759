from itertools import count


def generator(arg):
    for el in count(arg):
        if el == 10:
            break
        else:
            yield el


result = generator(4)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
