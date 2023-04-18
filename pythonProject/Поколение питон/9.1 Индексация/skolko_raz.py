s = input()
total_plus = 0
total_ast = 0
for c in range(len(s)):
    if '+' in s[c]:
        total_plus += 1
    if '*' in s[c]:
        total_ast += 1
print(f'Символ + встречается {total_plus} раз')
print(f'Символ * встречается {total_ast} раз')