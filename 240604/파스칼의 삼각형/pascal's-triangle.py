n = int(input())
array = [[0] * n for _ in range(n)]

for i in range(n):
    array[i][0] = 1
    array[i][i] = 1

for i in range(2, n):
    for j in range(1,n):
        array[i][j] = array[i-1][j-1] + array[i-1][j]

for i in range(n):
    for j in range(n):
        if array[i][j] != 0:
            print(array[i][j], end=" ")

    print()