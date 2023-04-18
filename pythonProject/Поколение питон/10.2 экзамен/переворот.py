s = input()
if s[0] == 'h' and s[len(s)-1] == 'h':
    print(s[len(s) -1: 0 : -1] + s[0])
else:
    print(s[: s.find('h')] + s[s.rfind('h')  : s.find('h') -1 : -1] + s[s.rfind('h') + 1:])