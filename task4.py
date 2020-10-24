# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.position = "Машина стоит"

    def Go(self):
        self.position = "Машина поехала!"

    def Stop(self):
        self.position = "Машина остановилась."

    def Turn_Left(self):
        self.position = "Машина повернула налево."

    def Turn_Right(self):
        self.position = "Машина повернула направо."

    def Show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed}")


class TownCar(Car):
    def Show_speed(self):
        if self.speed > 60:
            print(f"Превышена разрешенная скорость автомобиля 60 км/ч. Вам выписан штраф")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def Show_speed(self):
        if self.speed > 40:
            print(f"Превышена разрешенная скорость автомобиля 40 км/ч. Вам выписан штраф")
        else:
            print(f"Текущая скорость автомобиля {self.speed}")


class PoliceCar(Car):
    pass


car_1 = TownCar(65, "баклажан", "Приора")
print(car_1.name)
car_1.Go()
print(car_1.position)
car_1.Show_speed()
car_1.Turn_Left()
car_1.speed = 55
print(car_1.position)
car_1.Show_speed()

car_2 = WorkCar(40, "белый", "Киа")
car_1.Go()
print(car_2.name)
car_2.Go()
car_2.Turn_Right()
print(car_2.position)
car_2.Show_speed()

car_3 = SportCar(120, "Хаки", "Ниссан GTR")
print(car_3.name)
car_3.Go()
print(car_3.position)
car_3.Show_speed()
