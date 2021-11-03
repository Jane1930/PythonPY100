if __name__ == "__main__":
    #def palindrome_str():
     #   str_ = input("Введите строку: ")
      #  if str_ == str_[::-1]:
       #     print("Строка палиндром")
       # else:
         #   print("Строка не палиндром")

    def is_palindrome(str_):
        i = 0
        j = len(str_) - 1
        is_palindrome = True
        while i < j:
            if str_[i] != str_[j]:
                is_palindrome = False
            i += 1
            j -= 1
        return is_palindrome

str_ = input("Введите строку: ")
if is_palindrome(str_):
    print("Строка является палиндромом")
else:
    print("Строка НЕ является палиндромом")
