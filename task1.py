# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
from copy import deepcopy

class Matrix:
    def __init__(self, list_in_list: list):
        self.list_in_list = list_in_list

    def __str__(self):
        return f"{self.list_in_list}"

    def __add__(self, other):
        result = deepcopy(self.list_in_list)
        for i in range(len(self.list_in_list)):
            for j in range(len(self.list_in_list[0])):
                result[i][j] = self.list_in_list[i][j] + other.list_in_list[i][j]
        return Matrix(result)


el_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
el_2 = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
matrix_1 = Matrix(el_1)
matrix_2 = Matrix(el_2)
print(matrix_1)
print(matrix_2)
matrix_3 = matrix_1 + matrix_2
print(matrix_3)

