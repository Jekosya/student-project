n = int(input())
abc = []
s = ''
for _ in range(n):
    abc.append(input())
k = int(input())
for i in abc:
    if len(i) < k:
        continue
    s += i[k-1]
print(s)
