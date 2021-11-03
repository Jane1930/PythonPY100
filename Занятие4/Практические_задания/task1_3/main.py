if __name__ == "__main__":
    # inline_if = i ** 2 if i % 2 == 0  else -i   # тернарный оператор
    list_ = [i ** 2 if i % 2 == 0 else -i for i in range(10)]
    print(list_)


