ip_is_ok = True
for c in input().split('.'):
    if not 0 <= int(c) <= 255:
        ip_is_ok = False
if ip_is_ok:
    print('ДА')
else:
    print('НЕТ')