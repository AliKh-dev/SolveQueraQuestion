costs = [int(i) for i in input().split()]
n1 = [int(i) for i in input().split()]
n2 = [int(i) for i in input().split()]
n3 = [int(i) for i in input().split()]
max_numbers = max(max(n1), max(n2), max(n3))
min_numbers = min(min(n1), min(n2), min(n3))

sum_costs = 0
for i in range(min_numbers, max_numbers):
    cnt = 0
    if i >= min(n1) and i < max(n1):
        cnt += 1
    if i >= min(n2) and i < max(n2):
        cnt += 1
    if i >= min(n3) and i < max(n3):
        cnt += 1
    sum_costs += (costs[cnt - 1] * cnt)
    
print(sum_costs)
