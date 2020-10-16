from random import randint

checklist = [randint(1, 10) for el in range(20)]
print(checklist)
print([el for el in checklist if checklist.count(el) == 1])
