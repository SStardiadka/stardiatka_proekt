# роскомнадзор_запретил_букву
n1 = ' '.join(input()).split()
a = [' ', 'з', 'а', 'п', 'р', 'е', 'т', 'и','л', ' ', 'б', 'у', 'к', 'в', 'у', ' ']
b = ['з', 'а', 'п', 'р', 'е', 'т', 'и', 'л', 'б', 'у', 'к', 'в', 'у']
lst = n1 + a
lst1 = n1 + b
lst2 = sorted(set(lst1))
print(''.join(lst), lst2[0])
for i in range(len(lst2)-1):
    for j in lst:
        if lst2[i] == j:
            print(''.join(lst).strip(), lst2[i+1])
