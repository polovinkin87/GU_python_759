from random import randint

checklist = [randint(1, 100) for el in range(10)]
result_list = [checklist[el] for el in range(1, len(checklist)) if checklist[el] > checklist[el - 1]]
print(checklist)
print(result_list)
