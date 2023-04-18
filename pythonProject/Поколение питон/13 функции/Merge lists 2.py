def quick_merge (list):
    list = sorted(list, key=int)
    return list
abc = []
for i in range(int(input())):
    abc += (input().split())
s = quick_merge(abc)
print(*s)

