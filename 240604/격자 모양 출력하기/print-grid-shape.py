n, m = map(int, input().split())

array = [[0] * n for _ in range(n)]
place = []

for _ in range(m):
    place.append(list(map(int, input().split())))

for r,c in place:
    array[r-1][c-1] = r*c

for i in range(n):
    for j in range(n):
        print(array[i][j], end = " ")
    print()