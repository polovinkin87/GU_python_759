from functools import reduce

checklist = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(lambda args1, args2: args1 * args2, checklist))
