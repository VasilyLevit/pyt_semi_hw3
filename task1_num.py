# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv'] "7"

in_list = ['65h34q', 'sdg634d', '147jnbv']
find_n = '7'
for i in in_list:
    if find_n in i:
        print(i)