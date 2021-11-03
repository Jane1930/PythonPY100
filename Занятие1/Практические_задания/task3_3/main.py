number = 123

d_1 = number // 100
d_2 = number // 10 % 10
d_3 = number % 10

list_digit = [d_1, d_2, d_3]
print(list_digit)

print("Сумма цифр", sum(list_digit))
print("Количество цифр", len(list_digit))
print("Минимальная цифра", min(list_digit))
print("Максимальная цифра", max(list_digit))
