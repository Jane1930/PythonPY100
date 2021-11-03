if __name__ == "__main__":
    num = input("Введите число: ")
    list_digit = [int(d) for d in str(num)]
    print(list_digit)
    print(sum(list_digit))
    print(sum([d for d in list_digit if d % 2 == 0]))
    print(len(list_digit))
    print([list_digit[i] for i in range(len(list_digit)) if i % 2 == 0])
    print([list_digit[i] for i in range(len(list_digit)) if i % 2 != 0])
    print(list_digit[0] - list_digit[-1])
    for index, value in enumerate(list_digit):
        if value == min(list_digit):
            print(index)