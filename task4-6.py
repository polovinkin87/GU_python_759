# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
# и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру,
# например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.
from abc import ABC, abstractmethod


class Warehouse:
    address = "Red street"
    area = 11500
    state = 45
    cnt_car = 7
    type_property = "rent"
    hour_open = 9
    hour_close = 20


class ErrorInput(Exception):
    def __init__(self, text):
        self.text = text


class Office_technic(ABC):
    @abstractmethod
    def arrival(self, cnt_arriv):
        pass

    @abstractmethod
    def shipment(self, cnt_ship):
        pass


class Printer(Office_technic):
    material = "paper"
    cnt_print = 0

    def __init__(self, name, color, prod_date, prod_country, weight, speed):
        self.name = name
        self.color = color
        self.prod_date = prod_date
        self.prod_country = prod_country
        self.weight = weight
        self.speed = speed

    def arrival(self, cnt_arriv):
        try:
            if not str(cnt_arriv).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_print += cnt_arriv
            return f"Принято {cnt_arriv} принтеров на склад"

    def shipment(self, cnt_ship):
        try:
            if not str(cnt_ship).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_print -= cnt_ship
            return f"Отгрузили {cnt_ship} принтеров со склада"


class Scanner(Office_technic):
    cnt_scan = 0

    def __init__(self, name, color, prod_date, prod_country, weight):
        self.name = name
        self.color = color
        self.prod_date = prod_date
        self.prod_country = prod_country
        self.weight = weight

    def arrival(self, cnt_arriv):
        try:
            if not str(cnt_arriv).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_scan += cnt_arriv
            return f"Принято {cnt_arriv} сканеров на склад"

    def shipment(self, cnt_ship):
        try:
            if not str(cnt_ship).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_scan -= cnt_ship
            return f"Отгрузили {cnt_ship} сканеров со склада"


class Xerox(Office_technic):
    material = "paper"
    cnt_xerox = 0

    def __init__(self, name, color, prod_date, prod_country, weight, speed):
        self.name = name
        self.color = color
        self.prod_date = prod_date
        self.prod_country = prod_country
        self.weight = weight
        self.speed = speed

    def arrival(self, cnt_arriv):
        try:
            if not str(cnt_arriv).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_xerox += cnt_arriv
            return f"Принято {cnt_arriv} ксероксов на склад"

    def shipment(self, cnt_ship):
        try:
            if not str(cnt_ship).isdigit():
                raise ErrorInput("Ошибка ввода! Введите число!")
        except ErrorInput as err:
            print(err)
        else:
            self.cnt_xerox -= cnt_ship
            return f"Отгрузили {cnt_ship} ксероксов со склада"


pr = Printer("samsung", "white", 2019, "China", 8, 30)
sc = Scanner("hp", "blue", 2020, "China", 5)
xe = Xerox("samsung", "white", 2020, "China", 6, 50)
print(pr.arrival(200))
print(pr.cnt_print)
print(xe.arrival(400))
print(xe.shipment(150))
print(xe.cnt_xerox)
