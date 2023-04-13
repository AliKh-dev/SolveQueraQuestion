n = int(input())
code = input()
numbers = [0] * n
cnt = 0
for i in range(n):
    numbers[i] = input()
    if numbers[i].find(code[i]) >= 5:
        # print(numbers[i].find(code[i]))
        cnt += (9 - numbers[i].find(code[i]))
    else:
        # print(numbers[i].find(code[i]))
        cnt += numbers[i].find(code[i])
    # print("-----------")
print(cnt)
