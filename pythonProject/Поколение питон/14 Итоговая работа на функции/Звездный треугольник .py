def draw_triangle():
    for i in range (1, 9):
            print(' ' * (8 - i) + '*' * (i*2 - 1), end='')
            print ()

draw_triangle()