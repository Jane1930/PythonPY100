if __name__ == "__main__":
    # постарайтесь не использовать "магические" числа,
    # а по возможности дать переменным осмысленные названия и использовать

    for index, value in enumerate("Hello,world", start=5):
        print(index * ' ', value, sep='')
