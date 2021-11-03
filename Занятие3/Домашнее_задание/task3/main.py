if __name__ == "__main__":
    def max_word(str_):
        list_str = list(str_)
        list_index = []
        max_word_list = []
        count = 0
        for index in range(len(list_str)):
            list_index.append(len(list_str[index]))   # добавляем в список длины слов для того, чтобы определить наибольшее из них
        max_list_index = max(list_index)              # определяем максимальное значение в списке
        for num in list_index:                        # пробегаем по списку и ищем максимальные числа
            if num == max_list_index:
                count += 1                            # определяем количество максимальных чисел в списке
        if count == 1:
            for index, value in enumerate(list_index):
                if value == max_list_index:           # проходим по списку для определения значения и его индекса, и используем оиндек наибольшего значения для печати числа с макисмальной длиной из первого списка
                    return list_str[index]
        elif count > 1:
            for index, value in enumerate(list_index):
                if value == max_list_index:
                    max_word_list.append(list_str[index])
            return max_word_list


    str_ = input("Введите строку: ").split()
    print(max_word(str_))