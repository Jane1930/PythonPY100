def check_number(num):
    dict_num ={}
    for i in range(len(num) - 1):
        if num[i] in dict_num:
            dict_num[i] += 1
        else:
            dict_num[i] = 1
    for key, value in dict_num.items():
        if value > 1:
            return "Есть одинаковые цифры"
        else:
            return "Нет одинаковых цифр"

if __name__ == "__main__":
    num = input("Введите число: ")
    print(check_number(num))
