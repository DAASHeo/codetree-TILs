n = int(input())

dx = [-1,1]
dy = [-1,1]

path = [0, 0]
#동E서W남S북N
for i in range(n):
    a,b = map(str, input().split())
    if a == 'N':
        path[1] = path[1] + int(b) * dy[1]
    elif a == 'E':
        path[0] = path[0] + int(b) * dx[1]
    elif a == 'S':
        path[1] = path[1] + int(b) * dy[0]
    else:
        path[0] = path[0] + int(b) * dx[0]

print(' '.join(map(str,path)))