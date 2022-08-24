def fib_rec(N, f=[1]):
    for i in range(N-1):
        f.append(sum(f[i-1:]))
    s = str()
    for i in f:
        s += '!' + str(i)
        s = s.replace('!', ' ')
    return (s)


N = int(input())
fib_rec(N)