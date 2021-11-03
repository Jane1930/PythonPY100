if __name__ == "__main__":
    def task_1_1(n, m):
        return [i ** 2 for i in range(n, m + 1)]

    n = int(input("Введите число: "))
    m = int(input("Введите число: "))

    print(task_1_1(n, m))
