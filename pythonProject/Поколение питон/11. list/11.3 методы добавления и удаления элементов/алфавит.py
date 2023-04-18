abc = []
for i in range(ord('a'), ord('z')+1):
    abc.append(chr(i) * (i-ord('a') + 1))
print(abc)