# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: - [1.1, 1.2, 3.1, 10.01] => 0.19

in_list = [1.1, 1.2, 3.1, 10.01]
# Вариант 1
# max = min = in_list[0]%1

# for i in in_list[1::]:
#     if (i%1) > max:
#         max = i%1
#     elif (i%1) < min:
#         min = i%1
# print('max-min = ', round(max-min,2))

# Вариант 2 - с испльзованим LC от Тани
list_2 = list(map(lambda x: (x * 100 % 100), in_list))
print((max(list_2) - min(list_2)) / 100)