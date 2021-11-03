if __name__ == "__main__":
    def task_1_3(list_numbers):
        return sum([num for num in list_numbers if num % 2 == 0])
    list_numbers = [1, 4, 7, 6, 10, 5]
    print(task_1_3(list_numbers))

