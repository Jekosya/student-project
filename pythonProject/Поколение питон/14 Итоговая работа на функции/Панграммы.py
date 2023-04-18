def is_pangram(text):
    flag = True
    txt = text.lower()
    abc = "abcdefghijklmnopqrstuvwxyz"
    for i in range (len(abc)):
        if abc[i] not in  txt:
            flag = False
    return flag
text = input()
print(is_pangram(text))