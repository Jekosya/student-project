s, consonants, vowels  = input(), 0, 0
for c in range(len(s)):
    if s[c] in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
        vowels += 1
    if s[c] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
        consonants += 1
print('Количество гласных букв равно', vowels)
print('Количество согласных букв равно', consonants)
