n, m = map(int, input().split())
array = [[0] * n for i in range(n)]
coin = []

for _ in range(m):
    coin.append(list(map(int, input().split())))

for r,c in coin:
    array[r-1][c-1] = 1

for i in range(n):
    for j in range(n):
        print(array[i][j], end = " ")
    print()