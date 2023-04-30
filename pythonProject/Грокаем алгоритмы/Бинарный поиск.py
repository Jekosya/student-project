def binary_search (list, item):
    low = 0
    high  = len(list) - 1

    while low <= high:
        mid = int ((low + high) / 2)
        guess = list[mid]

        if guess == item:
            return list[mid]

        if guess < item:
            low = mid + 1

        else:
            high = mid - 1

    return 'Элемент не найден \n'

my_list = [12, 31, 22, 37, 41, 53, 62, 71, 228, 93]
sorted_num = sorted(my_list)

while True:
   find_me = int(input('Введите искомый элемент \n'))

   print (binary_search(sorted_num, find_me))
   answer = input('Если хоите повторить запрос, нажмите "д". Для выхода нажмите любую другу. кнопку\n')
   if answer == 'д':
       continue
   else:
       break
