def sum_in_range(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        total_sum += num
    return total_sum
start_range = int(input("Введіть початкове значення діапазону: "))
end_range = int(input("Введіть заключне значення діапазону: "))
result = sum_in_range(start_range, end_range)
print(f"Сума чисел у діапазоні від {start_range} до {end_range} дорівнює {result}.")
