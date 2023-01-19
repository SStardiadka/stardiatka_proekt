def sortdict(dk):
    return {i: dk[i] for i in sorted(dk, key= dk.get, reverse=True)}
print(sortdict({'qwe':21, 'wer': 7, 'ert': 8}))