# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

dec = 44
bin = []
while dec > 0:
    bin.insert(0, dec%2)
    dec //= 2
print(bin)