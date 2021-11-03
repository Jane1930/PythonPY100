A = int(input("Введите число: "))
B = int(input("Введите число: "))
C = int(input("Введите число: "))

result_1 = A < 45 and B >= 45 and C >= 45
result_2 = A >= 45 and B < 45 and C >= 45
result_3 = A >= 45 and B >= 45 and C < 45

if result_1 or result_2 or result_3:
    print("Условие истинно")
else:
    print("Условие не является истинным")
