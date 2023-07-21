# выодить фразу а не ошибку если нет ключа
from collections import defaultdict as df

dk1 = {
    "qw": 1,
    "qe": 2,
    "qr": 3,
}
dk = df(lambda: "нет ключа", dk1)
print(dk["1"])
