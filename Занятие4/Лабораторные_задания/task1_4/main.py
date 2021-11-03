if __name__ == "__main__":
    def task_1_4(list_numbers):
        return [num for num in list_numbers if num > sum(list_numbers) / len(list_numbers)]

    list_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
     print(task_1_4(list_numbers))
