n = int(input())
code = input()
numbers = [0] * n
cnt = 0
for i in range(n):
    numbers[i] = input()
    if numbers[i].index(code[(n-1) - i]) > (len(numbers[i]) // 2):
        cnt += len(numbers[i]) - numbers[i].index(code[(n-1) - i])
    else:    
        cnt += numbers[i].index(code[(n-1) - i])
print(cnt)