n, m = map(int,input().split())
if m < 3 or n < 3:
    print(0)
    quit()
table = [0] * n
for i in range(n):
    table[i] = [int(k) for k in input().split()]

# print("--------------")
cnt = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        # print(table[i][j], end=" ")
        if (table[i][j] > table[i - 1][j] and table[i][j] > table[i + 1][j]) and (table[i][j] < table[i][j - 1] and table[i][j] < table[i][j + 1]):
            cnt += 1
        elif (table[i][j] < table[i - 1][j] and table[i][j] < table[i + 1][j]) and (table[i][j] > table[i][j - 1] and table[i][j] > table[i][j + 1]):
            cnt += 1
    # print()

print(cnt)
# print(table)