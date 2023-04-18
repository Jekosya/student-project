n = int(input())
for i in range (n):
    if i == 0 or i == n-1:
        for j in range(19):
            print('*',end='')
    else:
        for j in range(19):
            if j == 0 or j == 18:
                print('*', end='')
            else:
                print(' ', end='')
    print()


