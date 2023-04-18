s = input()
x, y = s[:s.find('h')], s[s.rfind('h')+1:]
print(x,y, sep='')
