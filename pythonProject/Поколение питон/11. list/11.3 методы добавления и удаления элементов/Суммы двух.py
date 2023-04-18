n = int(input())
abc = []
x = 0
for i in range(n):
    num = int(input())
    abc.append(x + num)
    x = num
del (abc[0])
print(abc)