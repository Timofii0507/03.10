def output_even_num():
    start = int(input("Введіть початкове число: "))
    finish = int(input("Введіть кінцеве число: "))
    if start % 2 != 0:
        start += 1
    for num in range(start, finish + 1, 2):
        print(num)
output_even_num()
