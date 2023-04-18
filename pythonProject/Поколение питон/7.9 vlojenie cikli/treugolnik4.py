n = int(input())
for i in range(1, n+1):
    for j in range(1, i*2 // 2):
        print(j, end = '')
    for k in range(i*2 // 2, 0, -1):
        print(k, end = '')
    print()