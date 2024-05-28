n,m = map(int, input().split())

array = [[0] * m for _ in range(n)]
number = 0


for j in range(m):
    if j == 0 or j % 2 == 0:
        for i in range(n):
            array[i][j] = number
            number += 1
    else:
        for i in range(n-1, -1, -1):
            array[i][j] = number
            number += 1

for i in range(n):
    for j in range(m):
        print(array[i][j], end = " ")

    print()