n, m = map(int, input().split())
for i in range(3 * n):
    if i % (2 * n) >= n:
        print(m*"." + m*"X" + m*".")
    else:
        print(m*"X" + m*"." + m*"X")
