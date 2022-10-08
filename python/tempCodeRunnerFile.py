def china_animals(year):
    animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
    return year, animals[year % 12]

print(china_animals(int(input())))