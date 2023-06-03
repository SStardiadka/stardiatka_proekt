import itertools

n, k = map(int, input().split())
# k количество элементов - 2
lst = [*range(1, n + 1)]  # [1, 2, 3, 4]
combi = list(itertools.combinations(lst, k))
print(combi)  # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
print(len(combi))  # 6
