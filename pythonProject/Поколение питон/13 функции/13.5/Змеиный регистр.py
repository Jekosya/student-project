def convert_to_python_case(text):
    abc = list(text)
    snake = abc[0]
    for i in range(1, len(abc)-1):
        snake += abc[i]
        if abc[i + 1].isupper():
            snake += '_'
    snake += abc [-1]
    return snake.lower()
txt = input()
print(convert_to_python_case(txt))