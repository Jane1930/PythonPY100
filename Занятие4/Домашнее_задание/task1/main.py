def check_number(num):
    for i in range(len(num) - 1):
        if num[i] == num[i+1]:
            return "Все числа одинаковые"
        else:
            return "Все числа НЕ одинаковые"

if __name__ == "__main__":
    num = input("Введите число: ")
    print(check_number(num))