n = int(input())
code = int(input())
numbers = [0] * n
cnt = 0
for i in range(n):
    numbers[i] = input()
    key = str(code // 10 ** (n - (i+1)))
    # print(key)
    code %= 10 ** (n - (i+1))
    # print("key is ",key)
    if numbers[i].index(key) > (len(numbers[i]) // 2):
        cnt += len(numbers[i]) - numbers[i].index(key)
    else:    
        cnt += numbers[i].index(key)
print(cnt)