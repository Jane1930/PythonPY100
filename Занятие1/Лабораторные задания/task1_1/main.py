DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("Введите ваш год рождения: "))  # TODO запросить у пользователя год рождения
current_year = int(input("Текущий год: "))

print(DAYS_OF_YEAR * (current_year - start_year))# TODO посчитать и распечатать количество прожитых дней
