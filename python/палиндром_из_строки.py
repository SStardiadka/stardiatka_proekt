from collections import Counter


def palindrome_from_a_string(string: str) -> str:
    """
    На вход программы подается строка, содержащая заглавные латинские буквы
    (не обязательно различные)
    Разрешается переставлять буквы, а также удалять некоторые из них.
    Напишите программу, которая из данных букв по указанным правилам составит и выведет
    палиндром наибольшей длины, а если таких палиндромов несколько,
    то необходимо вывести первый из них в алфавитном порядке
    """
    dk = sorted(Counter(string).items())

    left_right = "".join(k * (v // 2) for k, v in dk)

    middle = "".join(k * (v % 2) for k, v in dk)

    return f"{left_right}{middle[:1]}{left_right[::-1]}"


print(palindrome_from_a_string(input()))

# def palindrome_from_a_string(string: str) -> str:
#     counter = [0] * 26

#     for i in string:
#         counter[ord(i) - ord('A')] += 1
#     result = midl = ''
#     for i in range(26):
#         result += chr(i + 65) * (counter[i] // 2)

#         if midl == '' and counter[i] % 2 == 1:
#             midl = chr(i + 65)
#     result = result + midl + result[::-1]
#     return(result)
