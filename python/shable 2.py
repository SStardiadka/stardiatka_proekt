str = input().split()# вводим наш список
str.sort()# сортируем его
l = len(str)# считаем количество елементов
for i in range(0,l - 1):# вводим интервал от 0 до (l-1 смотри строку(7))
     if str.count(str[i]) > 1 and str[i] != str[i + 1]:# через(count()) считаем количество элементов и если больше 1 
# то выводим результат как только меняется элемент(что бы избежать повторных выводов)
      print(str[i],end=' ')# если в конце списка больше 1 элемента то програма заглючит. по этому завершаем досрочно
# смотри строку(4)
for i in range(l-2,l-1):# вводим новый интервал(последних 2 елемента)
    if str[i] == str[i + 1] and l != 1:# если они равны и список не состоит из 1 элемента
     print(str[i],end=' ')# дописываем результат по последнему элементу!
