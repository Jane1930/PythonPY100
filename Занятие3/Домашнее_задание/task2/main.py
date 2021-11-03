def check_string(str_):
    base = set('01')

    for d in set(str_):  # выделяем все уникальные символы из строки
        if d not in base:
            return False
    return True


if __name__ == "__main__":
    # def is_binary_number(srt_):
    str_ = input("Введите строку: ")
    print(check_string(str_))