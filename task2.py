time = int(input("Введите количество секунд: "))
hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60
result = '%02d:%02d:%02d' % (hours, minutes, seconds)
print(result)
