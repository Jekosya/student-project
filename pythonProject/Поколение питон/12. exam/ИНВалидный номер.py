n = input().split('-')
flag = True
if len(n) != 3 and len(n) != 4:
    flag = False
elif len(n) == 4 and int(n[0]) != 7:
    flag = False
for i in n:
    if i.isdigit() == False:
        flag = False
if len(n) == 3 and len(n[0]) != 3 or len(n) == 3 and len(n[1]) != 3 or len(n) == 3 and len(n[2]) != 4 :
    flag = False
elif len(n) == 4 and len(n[1]) != 3 or len(n) == 4 and len(n[2]) != 3 or len(n) == 4 and len(n[3]) != 4:
    flag = False
if flag == False:
    print('NO')
else:
    print('YES')
