if __name__ == "__main__":
    def is_savings_eniugh(incomes, expenses, savings, inflation=1.05):
        mounths = 1
        current_incomes = savings + incomes * mounths
        current_expenses = expenses * mounths * (inflation ** (mounths - 1))
        while current_expenses + expenses * mounths * (inflation ** (mounths - 1)) < current_incomes + incomes * mounths :
            current_incomes = savings + incomes * mounths
            current_expenses = expenses * mounths * (inflation ** (mounths - 1))
            mounths += 1
        return mounths

    incomes = int(input("Введите размер стипендии: "))
    expenses = int(input("Введите размер расходов: "))
    savings = int(input("Введите размер сбережений: "))
    print(is_savings_eniugh(incomes, expenses, savings))


