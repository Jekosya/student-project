n = input()
s = []
new = []
for i in range(int(n[1:])):
    s.append(input())
for c in s:
    new.append(c[:c.find('      ')])
print(*new, sep ='\n')