s = input()
count = 0
if s.find('f') == -1:
    print(-2)
else:
    for c in range(s.find('f'), len(s)):
        if s.find('f') == s.rfind('f'):
            print('-1')
            break
        if s[c] == 'f':
            count += 1тест6.py
            if count == 2:
                print(c)