# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
# и умножение созданных экземпляров. Проверьте корректность полученного результата.

class Complex_Number:
    def __init__(self, number: str):
        self.number = number

    def __add__(self, other):
        x = self.number
        y = other.number
        real = int(x[0]) + int(y[0])
        imag = int(x[1:-2]) + int(y[1:-2])
        return Complex_Number(f"{real}+({imag})*i")

    def __mul__(self, other):
        x = self.number
        y = other.number
        res1 = int(x[0]) * int(y[0])
        res2 = int(x[1:-2]) * int(y[0])
        res3 = int(x[0]) * int(y[1:-2])
        res4 = int(x[1:-2]) * int(y[1:-2])
        return Complex_Number(f"{res1}+({res2}*i)+({res3}*i)+({res4}*i**2)")


a = Complex_Number("2+3*i")
b = Complex_Number("3-6*i")
c = a + b
d = a * b
print(c)
print(c.number)
print(d.number)
