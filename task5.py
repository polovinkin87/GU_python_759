# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def Draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def Draw(self):
        print(self.title)
        print("Рисуем рамку")


class Pencil(Stationery):
    def Draw(self):
        print(self.title)
        print("Рисуем объект")


class Handle(Stationery):
    def Draw(self):
        print(self.title)
        print("Запуск заливки цветом")


station_1 = Stationery("Бумага")
print(station_1.title)
station_1.Draw()
station_2 = Pen("Шариковая ручка")
station_2.Draw()
station_3 = Pencil("Черный карандаш")
station_3.Draw()
station_4 = Handle("Красный маркер")
station_4.Draw()
