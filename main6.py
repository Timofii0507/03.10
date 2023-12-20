def count_digits(number):
    number_str = str(number)
    return len(number_str)
input_number = input("Введіть число: ")
try:
    input_number = float(input_number)
    if input_number.is_integer():
        input_number = int(input_number)
    else:
        raise ValueError("Введіть ціле число.")
except ValueError:
    print("Помилка! Будь ласка, введіть правильне число.")
    exit()
result = count_digits(input_number)
print(f"Кількість цифр у числі {input_number}: {result}")
