text = 'aaaa'
b = 'aa'
import re
match = [i.start() for i  in re.finditer(rf'(?=({b}))', text)]
match1 = [i.end() for i  in re.finditer(rf'(?<=({b}))', text)]
print(list(match))
print(list(match1))
print(*list(zip(list(match), list(match1))))