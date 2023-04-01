n = int(input())
numbers = [0] * n
sum_number = 0
for i in range(n):
    numbers[i] = int(input())
    sum_number += numbers[i]
average = sum_number // n
result = 0
for number in numbers:
    result += (abs(number - average))
print(result // 2)
