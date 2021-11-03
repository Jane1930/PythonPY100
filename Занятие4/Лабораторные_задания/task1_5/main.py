if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    even_integers = [even for even in list_ if even % 2 == 0]
    odd_integers = [odd for odd in list_ if odd % 2 != 0]
    if len(even_integers) > len(odd_integers):
        print("Больше четных чисел")
    elif len(even_integers) < len(odd_integers):
        print("Больше НЕчетных чисел")
    else:
        print("Равное количество")
