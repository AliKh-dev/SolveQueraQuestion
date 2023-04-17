x = int(input())
n = int(input())
if n == 0:
    print(20)
elif n == 7:
    print(x)
else:
    if x - n < 0:
        x = 0
    else:
        x -= n
    print(x)
