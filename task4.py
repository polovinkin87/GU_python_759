number = int(input("Введите целое положительное число: "))
mod = number % 10
div = number // 10
while div != 0:
    mod_2 = div % 10
    if mod < mod_2:
        mod = mod_2
    div = div // 10

result = f"Наибольшая цифра в числе: {mod}"
print(result)
