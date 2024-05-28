n, m = map(int, input().split())
array_1 = [list(map(int, input().split())) for _ in range(n)]
array_2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if array_1[i][j] == array_2[i][j]:
            print("0", end = " ")
        else:
            print("1", end = " ")
    print()