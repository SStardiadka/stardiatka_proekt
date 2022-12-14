def frequency_sort(items):
    #  посчитать сколько раз элемент встречается в списке
    lst1 = []
    # a = items.count
    # dk = {k: a(k)  for k in items}
    ls = sorted(items, key=lambda x: (-items.count(x), items.index(x)))
    # for i in ls:
    #     for k, v in dk.items():
    #         if i == k:
    #             for j in range(v):
    #                 lst1.append(k)
    return ls
    
print(frequency_sort([4, 6, 2, 2, 2, 6, 4, 4, 4]))