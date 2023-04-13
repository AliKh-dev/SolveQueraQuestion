n1, n2, n3 = input().split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
if n1 in range(1, 180):
    if n2 in range(1, 180):
        if n3 in range(1, 180):
            num = n1+n2+n3
            if num == 180:
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
