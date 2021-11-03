def needed_saving(incomes, expenses, mounths=10, inflation=1.03):
    saivings = mounths * expenses * (inflation ** (mounths - 1)) - mounths * incomes

    return saivings


if __name__ == "__main__":
    incomes = int(input("Введите доход: "))
    expenses = int(input("Введите расход: "))
    print(needed_saving(incomes, expenses, mounths=10, inflation=1.03))


