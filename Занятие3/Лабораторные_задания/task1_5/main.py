def sum_positive_num():
    list_num = []
    sum_num = 0
    while True:
        num = int(input("ведите число: "))
        if num == 0:
            break
        list_num.append(num)
    for num in list_num:
        if num > 0:
            sum_num += num
    return sum_num

if __name__ == "__main__":
    print(sum_positive_num())
