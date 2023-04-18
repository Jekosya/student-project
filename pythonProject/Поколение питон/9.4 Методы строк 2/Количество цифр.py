s = input()
count = 0
for c in range(len(s)):
    if s[c] in '1234567890':
        count += 1
print(count)
