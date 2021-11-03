if __name__ == "__main__":
    list_ = [1, 4, 28, 3, 10, 0, 1]
    max_list = max(list_)
    for index, value in enumerate(list_):
        if value == max_list:
            max_index = int(index)
    list_[0], list_[max_index] = list_[max_index], list_[0]
    print(list_)
