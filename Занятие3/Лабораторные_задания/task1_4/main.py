def sum_of_infinity_series(epsilon=0.0001):
    n = 1
    current_sum = 0
    while True:
        current_value = 1 / (2 ** n)
        if current_value < epsilon:
            break
        current_sum = current_sum + current_value
        n += 1
    return current_sum, current_value


if __name__ == "__main__":
    print(sum_of_infinity_series())
