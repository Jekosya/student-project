txt = input()
abc = list(txt)
fin = abc[0]
for i in range (1, len(abc) - 1):
    fin += abc[i]
    if abc[i+1].isupper():
        fin += '_'
print(fin.lower())