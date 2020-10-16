from itertools import cycle


def generator(arg):
    s = 0
    for el in cycle(arg):
        if s > 15:
            break
        else:
            yield el
        s += 1


text = 'python'
result = generator(text)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
