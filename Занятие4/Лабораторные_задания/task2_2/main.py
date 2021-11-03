def check_number(num):
    base1 = "48"
    base3 = "9"
    for n in set(num):
        if n not in base1 or base3:
            return False
    return True

if __name__ == "__main__":
    num = input("Введите число: ")
    print(check_number(num))

