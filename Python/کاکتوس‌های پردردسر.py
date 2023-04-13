n = int(input())
groups = [int(i) for i in input().split()]
for i in range(n):
    if groups[i] <= 3:
        print('*' * groups[i])
        continue
    print('*')