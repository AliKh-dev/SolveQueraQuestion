n = int(input())
while True:
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    n = sum
    if sum < 10:
        break
print(sum)