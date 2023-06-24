from functools import total_ordering

"""
Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
__lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

"""


@total_ordering
class NaiveStudent:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def __eq__(self, other):
        return self.last_name == other.last_name

    def __lt__(self, other):
        return self.last_name < other.last_name


cl1 = NaiveStudent(1, 3)
cl2 = NaiveStudent(2, 4)
print(cl1 <= cl2)
