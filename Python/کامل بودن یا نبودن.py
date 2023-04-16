def sum_divisor(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum


num = int(input())
if sum_divisor(num) == num:
    print("YES")
else:
    print("NO")
