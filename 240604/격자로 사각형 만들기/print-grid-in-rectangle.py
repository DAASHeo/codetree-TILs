n = int(input())
array = [[0] * n for _ in range(n)]

for i in range(n):
    array[0][i] = 1
    array[i][0] = 1

for i in range(1, n):
    for j in range(1, n):
        array[i][j] = array[i-1][j] + array[i-1][j-1] + array[i][j-1]

for i in range(n):
    for j in range(n):
        print(array[i][j], end=" ")

    print()