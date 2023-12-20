def find_minimum():
    num = [float(input("Введіть число {}: ".format(i + 1))) for i in range(5)]
    minimum = min(num)
    return minimum
result = find_minimum()
print("Мінімальне число: {}".format(result))
