def draw_line(length, direction, symbol):
    if direction == 'горизонтальна':
        print(symbol * length)
    elif direction == 'вертикальна':
        for _ in range(length):
            print(symbol)
    else:
        print("Невірний напрямок. Використовуйте 'горизонтальна' або 'вертикальна'.")
length = int(input("Введіть довжину лінії: "))
direction = input("Введіть напрямок ('горизонтальна' або 'вертикальна'): ")
symbol = input("Введіть символ: ")
draw_line(length, direction, symbol)