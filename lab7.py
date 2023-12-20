def is_lucky_number(number):
    str_number = str(number)
    if len(str_number) != 6:
        return False
    first_half_sum = sum(map(int, str_number[:3]))
    second_half_sum = sum(map(int, str_number[3:]))
    return first_half_sum == second_half_sum
user_number = int(input("Введіть шестизначне число для перевірки: "))
result = is_lucky_number(user_number)
print(f"Число {user_number} {'є' if result else 'не є'} щасливим.")
