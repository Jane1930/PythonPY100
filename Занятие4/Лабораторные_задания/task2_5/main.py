def is_palindrome(num):
    return "Палиндром" if str(num) == str(num)[::-1] else "НЕ палиндром"

if __name__ == "__main__":
    num = input("Введите число: ")
    print(is_palindrome(num))
