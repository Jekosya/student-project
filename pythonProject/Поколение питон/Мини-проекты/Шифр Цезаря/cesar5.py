abc = input('Введите текст\n')

def hide_ENG(s):
    ent = ""
    s = s.split()

    for c in s:

        for j in c:
            temp = 0
            for k in c:
                if k.isalpha() == True:
                    temp += 1

            if ord(j) > 96 and ord(j) < 123:
                ent += chr(ord(j) + temp)
                if (ord(j) + temp) > 122:
                    ent = ent[:-1] + chr (97 + ((ord(j) + temp) - 123))
            elif ord(j) > 64 and ord(j) < 91:
                ent += chr(ord(j) + temp)
                if (ord(j) + temp) > 90:
                    ent = ent[:-1] + chr (65 + ((ord(j) + temp) - 91))
            if ord(j) < 65 or ord(j) > 90 and ord(j) < 97 or ord(j) > 122:
                ent += chr(ord(j))

        ent += " "

    return ent


print (hide_ENG(abc))