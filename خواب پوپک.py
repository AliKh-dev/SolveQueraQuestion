def divisor(number):
    divisors = list()
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors


a, b, x = map(int, input().split())
# print(divisor(a), divisor(b))
cnt_sleeps = 0
for i in divisor(a):
    for j in divisor(b):
        if i + j <= x:
            cnt_sleeps += 1
print(cnt_sleeps)
