n, y = map(int, input().split())

for n1 in range(n+1):
    for n2 in range(n-n1+1):
        n3 = n - n1 - n2

        if (n1 * 1000 + n2 * 5000 + n3 * 10000) == y:
            print(n3, n2, n1)
            exit()
else:
    print(-1, -1, -1)