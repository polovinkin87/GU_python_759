def my_func(var_1, var_2):
    res = 1 / var_1
    el = 1
    while el < abs(var_2):
        res *= 1 / var_1
        el += 1
    return res


print(my_func(4, -4))
print(pow(4, -4))
print(4**-4)
