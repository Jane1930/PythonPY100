if __name__ == "__main__":
    matrix = [
        [i * j for j in range(1, 10)] for i in range(1, 10)
    ]

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            value_ceil = matrix[row][col]
            print(f"{value_ceil:3}", end="\t")  # выбираем цифру 2 или 3 в зависимости от размера цифр двух или трех значные
        print()
