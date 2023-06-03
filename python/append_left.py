# позволяет добавлять и удалять элементы с обоих концов очереди.
from collections import deque

a = deque(["qwerty", "erty"])
a.append("bn")
a.appendleft("mn")
print(list(a))  #  ['mn', 'qwerty', 'erty', 'bn']
