n = int(input())

array = [[0] * n for _ in range(n)]
number = 1

if n % 2 != 0 :
    for j in range(n-1, -1, -1):
        if j % 2 != 0:
            for i in range(n):
                array[i][j] = number
                number += 1
            
        else:
            for i in range(n-1, -1, -1):
                array[i][j] = number
                number += 1
else:
    for j in range(n-1, -1, -1):
        if j % 2 == 0:
            for i in range(n):
                array[i][j] = number
                number += 1
            
        else:
            for i in range(n-1, -1, -1):
                array[i][j] = number
                number += 1
for i in range(n):
    for j in range(n):
        print(array[i][j], end = " ")
    print()