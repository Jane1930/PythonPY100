# 1**1 + 2*2
def main():
    num = 1
    current_sum = 0
    max_sum = 500
    while True:
        current_value = num ** 2
        if current_sum + current_value >= max_sum: # как только превышает условия, то это условие не выполняется
            break                                  # и число увеличивать не надо
        current_sum = current_sum + current_value
        num += 1
    print(num, current_sum)


if __name__ == "__main__":
    print(main())
