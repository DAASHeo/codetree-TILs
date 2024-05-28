import sys
array = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
result = []
for i in range(3):
    for j in range(i+1,4):
        array[i][j] = 0

for i in array:
    result.append(sum(i))


print(sum(result))