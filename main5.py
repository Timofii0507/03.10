def product_of_range(a, b):
  if a > b:
    a, b = b, a
  product = 1
  for i in range(a, b + 1):
    product = product * i
    return product
a = int(input("Введіть нижню межу діапазону: "))
b = int(input("Введіть верхню межу діапазону: "))
result = product_of_range(a, b)
print(f"Добуток чисел у діапазоні від {a} до {b} дорівнює {result}")
