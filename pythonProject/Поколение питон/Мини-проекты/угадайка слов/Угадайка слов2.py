import random
world_list = ['атака', 'бордюр', 'яблоко']

def get_word(x):
    word = random.choice(x)
    return (word.upper())

slovo = get_word(world_list)

print(slovo)

