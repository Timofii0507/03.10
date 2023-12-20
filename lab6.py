def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True
user_number = int(input("Введіть число для перевірки: "))
result = is_prime(user_number)
print(f"Число {user_number} {'є' if result else 'не є'} простим.")
