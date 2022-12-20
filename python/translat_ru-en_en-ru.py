# рускую расладку в английскую и на оборот
# функция  новая_строка = str.maketrans(шаблон, замена_шаблона)
# вывод print(старая_строка.translate(новая_строка))
eng_layout = "qwertyuiop[]asdfghjkl;'zxcvbnm,.`"
rus_layout = "йцукенгшщзхъфывапролджэячсмитьбюё"
s = input()
if s[0] in eng_layout:
    table = str.maketrans(eng_layout, rus_layout)
else:
    table = str.maketrans(rus_layout, eng_layout)
print(s.translate(table))