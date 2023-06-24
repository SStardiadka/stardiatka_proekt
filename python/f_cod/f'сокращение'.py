def truncate(text, length):
    result = f"{text[0:length]}..."
    return result
# результат работы функции
slovo = 'сокращение'
print(truncate(slovo,4))
