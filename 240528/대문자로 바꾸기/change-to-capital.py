import sys
array = [list(map(str, sys.stdin.readline().split())) for _ in range(5)]

for i in range(5):
    for j in range(3):
        print(array[i][j].upper(), end=" ")
    print()