from math import ceil
s = input()
h = ceil(len(s)/2)
print(s[h:], s[:h], sep = '')