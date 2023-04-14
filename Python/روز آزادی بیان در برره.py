count_bala = 1
count_pain = 2
k = int(input())
while True:
    if count_bala == k:
        print('Payin Barare')
        break
    elif count_pain == k:
        print('Bala Barare')
        break
    count_bala += 2
    count_pain += 2
