import sys
array = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
height = [0] * 4
total = 0

for i in array:
    total += sum(i)
    print(float(sum(i)/len(i)), end = " ")
print()

for i in range(4):
    for j in range(2):
        height[i] += array[j][i]
    print(float(height[i] / 2), end = " ")
print()

print(round(float(total / (2 * 4)),1))