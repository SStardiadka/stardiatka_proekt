from timeit import timeit

sts = ["1111:123", "1112:1234", "1114:1234", "1115:1234"] * 10000


def palindrome_from_a_string1(string):
    return len(dict([i.split(":") for i in string]))


print(
    f"""{timeit("palindrome_from_a_string1(sts)",globals=globals(),number=500,) / 500}
      [i.split(':') for i in string]"""
)


def palindrome_from_a_string2(string):
    return len(dict(i.split(":") for i in string))


print(
    f"""{timeit("palindrome_from_a_string2(sts)",globals=globals(),number=500,) / 500}
      (i.split(':') for i in string)"""
)


def palindrome_from_a_string3(string):
    return len(dict(map(lambda x: x.split(":"), string)))


print(
    f"""{timeit("palindrome_from_a_string2(sts)",globals=globals(),number=500,) / 500}
      (map(lambda x: x.split(':'), string)"""
)
