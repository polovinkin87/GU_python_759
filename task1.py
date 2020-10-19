with open("user_text.txt", "w") as f_obj:
    while True:
        text = input("Введите слово: ")
        f_obj.write(f"{text}\n")
        if not text:
            break
