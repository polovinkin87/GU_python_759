def user(name, surname, year, city, email, phone):
    return f"Данные пользователя: {name} {surname} {year} {city} {email} {phone}"


text_1 = input("Введите имя: ")
text_2 = input("Введите фамилию: ")
text_3 = input("Введите год рождения: ")
text_4 = input("Введите город проживания: ")
text_5 = input("Введите email: ")
text_6 = input("Введите телефон: ")

print(user(name=text_1, surname=text_2, year=text_3, city=text_4, email=text_5, phone=text_6))
