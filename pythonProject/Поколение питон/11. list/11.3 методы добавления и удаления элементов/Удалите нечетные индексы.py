n = int(input())
abc = []
for _ in range(n):
    abc.append(int(input()))
del(abc[1::2])
print(abc)