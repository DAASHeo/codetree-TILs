n, m = map(int, input().split())
point = 1
place = []
array = [[0] * n for i in range(n)]

for i in range(m):
    place.append(list(map(int, input().split())))
    place[i].append(point)
    point += 1

for r, c, p in place:
    array[r-1][c-1] = p

for i in range(n):
    for j in range(n):
        print(array[i][j], end=" ")
    print()