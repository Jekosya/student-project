n = int(input())
for a in range (1, 151):
    for b in range (a,151):
        for c in range (b,151):
            for d in range (c,151):
                for e in range (d, 151):
                    if a ** n + b ** n + c ** n + d ** n == e ** 5:
                        print(a+b+c+d+e)
                        break
