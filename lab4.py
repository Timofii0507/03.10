def find_maximum(a, b, c, d):
    max_number = max_from_pair(a, b)
    max_number = max_from_pair(max_number, c)
    max_number = max_from_pair(max_number, d)
    return max_number
def max_from_pair(x, y):
    if x > y:
        return x
    else:
        return y
number1 = float(input("Введіть перше число: "))
number2 = float(input("Введіть друге число: "))
number3 = float(input("Введіть третє число: "))
number4 = float(input("Введіть четверте число: "))
result = find_maximum(number1, number2, number3, number4)
print("Максимальне число: ", result)
