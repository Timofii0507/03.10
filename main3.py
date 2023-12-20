def draw_square(side_length, fill_symbol, filled):
    if filled:
        for _ in range(side_length):
            print(fill_symbol * side_length)
    else:
        print(fill_symbol * side_length)
        for _ in range(side_length - 2):
            print(fill_symbol + ' ' * (side_length - 2) + fill_symbol)
        print(fill_symbol * side_length)
side_length = int(input("Введіть довжину сторони квадрата (ціле число більше або рівне 2): "))
fill_symbol = input("Введіть символ для заповнення квадрата: ")
filled_square = input("Введіть 'True', якщо квадрат повинен бути заповненим, або 'False' в іншому випадку: ").lower() == 'true'
draw_square(side_length, fill_symbol, filled_square)
