#  Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#  Пример: список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

in_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
find_string = "qwe"
# count = -1
# for i in in_list:
#     if i == find_string:
#         count += 1
#         if count == 2:
#             
# print(count)

count = 0
for i in range(len(in_list)):
    if in_list[i] == find_string:
        count += 1
        if count == 2:
            print(i)
            continue
if count < 2:
    print('-1')