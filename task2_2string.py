#  Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
#  Пример: список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3

in_list = ["qwe", "asd", "zxc", "qwe", "ertqwe", "qwe"]
find_list = "qwe"
count = -1
for i in in_list:
    if i == find_list:
        count += 1
        if count == 1:
            print(i)
print(count)