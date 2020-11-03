# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date: str):
        self.date = date

    @staticmethod
    def in_number(element):
        temp = [int(el) for el in element.date.split("-")]
        return temp

    @staticmethod
    def valid(element):
        temp = [int(el) for el in element.date.split("-")]
        if temp[0] > 31:
            return f"Дни введены некорректно"
        elif temp[1] > 12:
            return f"Месяц введен некорректно"
        elif len(str(temp[2])) != 4:
            return f"Год введен некорректно"
        else:
            return f"Дата корректна"


d = Date("29-10-2020")
print(d.date)
print(d.in_number(Date("01-10-2020")))
print(d.valid(Date("01-10-2020")))
