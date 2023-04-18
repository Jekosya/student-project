def is_correct_bracket(text):
    open = 0
    clos = 0
    for c in text:
        if c == '(':
            open += 1
        if c == ')':
            clos += 1
        if clos > open:
            return False
    return open == clos
txt = input()
print(is_correct_bracket(txt))