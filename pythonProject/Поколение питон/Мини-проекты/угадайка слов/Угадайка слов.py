import random
world_list = ['атака', 'бордюр', 'яблоко']

def get_word(x):
    word = random.choice(x)
    return (word.upper())

tries = 6
def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / \/
        |
        |  ПИЗДЕЦ!

        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    / 
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|/
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    \|
        |     |
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |     
        |  
        ''',
        '''
        _______
        |     |
        |     O
        |    
        |     
        |    
        |  
        ''',
        '''
        _______
        |     |
        |     
        |    
        |       
        |  
        '''
    ]
    return stages[tries]

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')


    while True:
        print(display_hangman(tries))
        print(word_completion)
        letters = input('Введите букву или слово').upper()
        if letters.isalpha() == False:
            print('Вы ввели неверный символ')
            continue
        elif letters in guessed_words:
            print('Вы уже вводили это слово')
            continue
        elif letters in guessed_letters:
            print('Вы уже вводили эту букву')
            continue

        if len(letters) == 1 and letters in word:
            for i in range(len(word)):
                if word[i].upper() == letters.upper():
                    word_completion = word_completion[:i] + letters + word_completion[i + 1:]
            print('Вы угадали букву')
        if len(letters) == len(word) and letters in word:
            word_completion = word
            print('Поздравляем, вы угадали слово! Вы победили!')
            print(word_completion)
            break

        if len(letters) == 1 and letters not in word:
            print('Вы не угадали букву!')
            guessed_letters.append(letters)
            tries -= 1

        if len(letters) > 1 and letters not in word:
            print('Вы не угадали слово!')
            guessed_words.append(letters)
            tries -= 1

        if tries == 0:
            print('Вы не угадали слово \n')
            print(word)
            break





play(get_word(world_list))


