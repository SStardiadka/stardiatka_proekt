def short_in_long(my_list):  # вывести подсписок с минимальной или максимальной длинной
    a = min(map(len, my_list))
    for i in my_list:
        if len(i) == a:
            return i


print(short_in_long([[1, 7, 12, 0, 9, 100], ['a', 'b']]))
