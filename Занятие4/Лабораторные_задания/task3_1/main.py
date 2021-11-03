def get_frequency(main_str):
    main_str = main_str.lower()
    char_dict = {}

    for char in main_str:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    return  char_dict

def percentage_dict(dict_):
    total_count = sum(dict_.values())
    for key, value in dict_.items():         # {char: round(value / total_count, 3 for char, value in dict_.items()}
        dict_[key] = round(value / total_count, 3)
    return dict_

if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """
    dict_ = get_frequency(main_str)
    print(get_frequency(main_str))
    print(percentage_dict(dict_))
