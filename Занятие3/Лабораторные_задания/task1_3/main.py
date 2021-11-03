def factoring(num):
    list_ = []
    for current_number in range(1, num + 1):
        if num % current_number == 0 and current_number % current_number == 0:
            list_.append(current_number)
    return list_

if __name__ == "__main__":
    n = int(input("Bведите число: "))
    print(factoring(num))
