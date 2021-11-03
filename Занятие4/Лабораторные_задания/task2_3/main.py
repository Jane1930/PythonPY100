def check_number(num):
    list_digit = [int(n) for n in str(num)]
    final_num = sum(list_digit)
    final_num = str(final_num)
    list_final_num = list(final_num)
    return "Сумма чисел трехзначного числа - двухзначное число" if len(list_final_num) == 2 else "НЕ двухзначное"


if __name__ == "__main__":
    num = input("Введите число: ")
    print(check_number(num))