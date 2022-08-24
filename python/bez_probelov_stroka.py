def is_pangram(text):
    tx = text.split()
    tx = ''.join(tx)
    return tx

print(is_pangram('убрать пробели из строки'))