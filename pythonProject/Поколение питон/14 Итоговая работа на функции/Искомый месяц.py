def get_month(language, number):
    m_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
                 'ноябрь', 'декабрь']

    m_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                 'november', 'december']
    if language == 'ru':
        return m_ru[number-1]
    elif language == 'en':
        return m_en[number-1]
    else:
        return 'Вы ввели неверные данные'
lan = input()
num = int(input())
print(get_month(lan, num))