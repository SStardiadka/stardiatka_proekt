#  статик_модуль
import statistics

ls = 8

mean = sum(ls) / len(ls)
print(mean, statistics.mean(ls)) # стандартные (среднеквадратические) отклонения

variance = sum((x - mean) ** 2 for x in ls) / (len(ls) - 1)
print(variance, statistics.variance(ls)) #

stdev = variance ** (1 / 2)
print(stdev, statistics.stdev(ls)) # дисперсия