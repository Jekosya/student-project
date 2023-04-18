s = input()
large = 0
res = ''
chr = '0123456789АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯяABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
for c in range(len(chr)):
    if s.count(chr[c]) >= large:
        large = s.count(chr[c])
        res = chr[c]
print(res)