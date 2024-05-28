array_1 = [list(map(int, input().split())) for _ in range(3)]
input()
array_2 = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    for j in range(3):
        print(array_1[i][j] * array_2[i][j], end=" ")
    print()