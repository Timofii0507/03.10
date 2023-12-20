def print_odd_numbers():
    start = int(input("Введіть початкове число: "))
    end = int(input("Введіть кінцеве число: "))
    if start > end:
        start, end = end, start
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)
print_odd_numbers()