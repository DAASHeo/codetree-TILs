array = [[0] * 5 for i in range(5)]

for i in range(5):
    array[0][i] = 1
    array[i][0] = 1

for i in range(1, 5):
    for j in range(1, 5):
        array[i][j] = array[i-1][j] + array[i][j-1]

for i in range(5):
    for j in range(5):
        print(array[i][j], end=" ")

    print()