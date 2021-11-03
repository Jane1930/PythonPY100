def check_number(num):
    sum_digits_num = sum([int(n) for n in str(num)])
    return "Кратно" if sum_digits_num % 7 == 0 else "НЕ кратно"

if __name__ == "__main__":
    num = input("Введите число: ")
    print(check_number(num))

