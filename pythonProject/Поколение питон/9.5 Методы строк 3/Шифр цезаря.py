n = int(input())
s = input()
for c in range(len(s)):
    x = ord(s[c]) - n
    if x < 97:
       x = 123 - (97 - x)
    print(chr(x), end="")


