s = input().split()
count = 0
for c in s:
    if len(c) == 1 and 'a' in c.lower():
        count += 1
    if len(c) == 2 and 'an' in c.lower():
        count += 1
    if len(c) == 3 and 'the' in c.lower():
        count += 1
print('Общее количество артиклей:', count)