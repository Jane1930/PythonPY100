if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    average = sum(list_) / len(list_)
    print([(num - average) for num in list_])