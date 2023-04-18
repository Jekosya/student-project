count = 0
s = input().split()
copy = s
for i in range(len(s)):
    if i == s[i]:
        count+=1
print(count)