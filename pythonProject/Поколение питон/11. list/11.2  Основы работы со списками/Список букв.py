n = int(input())
alphabet = list(range(ord(chr(97)), ord(chr(123))))
abc = list()
for i in range (n):
    abc += list(chr(alphabet[i]))
print(abc)