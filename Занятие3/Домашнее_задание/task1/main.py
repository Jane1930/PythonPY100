if __name__ == "__main__":
    num_list = []
    while True:
        num = int(input("Введите число: "))
        if num < 0:
            break
        if 3 <= num <= 13:
            num_list.append(num)
    print(num_list)

