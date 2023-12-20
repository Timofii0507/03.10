def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]
input_number = int(input("Введіть число: "))
if is_palindrome(input_number):
    print(f"{input_number} є паліндромом")
else:
    print(f"{input_number} не є паліндромом")
