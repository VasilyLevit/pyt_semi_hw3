# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];  - [2, 3, 5, 6] => [12, 15]

input_list = [2, 3, 4, 5, 6]
out_list = []
len_list = len(input_list)
for i in range(0, len_list - len_list // 2):
    out_list.append(input_list[i] * input_list[-i-1])
print(out_list)