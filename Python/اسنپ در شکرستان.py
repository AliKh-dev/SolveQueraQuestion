n, m = map(int,input().split())
list_costs = [0] * n
for i in range(n):
    list_costs[i] = [int(k) for k in input().split()]

list_trips = [0] * m
for i in range(m):
    list_trips[i] = [int(k) for k in input().split()]

sum_cost = 0
for trip in list_trips:
    sum_cost += list_costs[trip[0] - 1][trip[1] - 1]

print(sum_cost)
# print()
# print(list_trips)
# print(list_costs)