array = [
    list(map(int, input().split()))
    for _ in range(4)
]

for i in array:
    print(sum(i))