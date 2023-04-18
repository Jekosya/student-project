s = input()
count = 0
for c in range(len(s)):
    if s[c] == 'f':
        count +=1
if count == 1:
    print(s.find('f'))
elif count >= 2:
    print(s.find('f'), s.rfind('f'))
else:
    print('NO')
