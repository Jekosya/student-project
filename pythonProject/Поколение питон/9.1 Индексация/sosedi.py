s = input()
temp = 'xx'
count = 0
for c in range(len(s)):
    if s[c] == temp:
        count += 1
    temp = s[c]
print(count)