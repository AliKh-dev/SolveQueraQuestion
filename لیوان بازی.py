n, x = input().split()
for i in range(int(n)):
    move1, move2 = input().split()
    if move1 == x:
        x = move2
    elif move2 == x:
        x = move1
print(x)
