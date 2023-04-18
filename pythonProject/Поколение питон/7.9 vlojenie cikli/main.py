n = int(input())
for bull in range (0, 11):
    for cow in range (1, 21):
        for baby_cow in range (1, 201):
            if 10 * bull + 5 * cow + 0.5 * baby_cow == 100:
                print('быки', bull, 'коровы', cow, 'телята', baby_cow)
                if bull + cow + baby_cow == 100:
                    print('Кол-во: быки', bull, 'коровы', cow, 'телята', baby_cow)
print()