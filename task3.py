# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    _income = {"wage": 45000, "bonus": 20000}

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    def Get_full_name(self):
        return f"{self.name} {self.surname}"

    def Get_total_income(self):
        return Worker._income["wage"] + Worker._income["bonus"]


manager = Position("Дима", "Петров", "менеджер")
print(manager.Get_full_name())
print(manager.Get_total_income())

analitik = Position("Александр", "Ручкин", "аналитик")
print(analitik.position)
print(analitik.Get_full_name())
print(analitik.Get_total_income())
