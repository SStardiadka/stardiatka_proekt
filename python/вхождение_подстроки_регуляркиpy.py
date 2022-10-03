text = 'aaaa'
b = 'aa'
import re
match = [i.start() for i  in re.finditer(rf'(?=({b}))', text)]
match1 = [i.end() for i  in re.finditer(rf'(?<=({b}))', text)]
print(match)
print(match1)
print(*zip(list(match), list(match1)))