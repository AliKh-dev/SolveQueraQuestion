n, m = map(int, input().split())
n_days = list()
m_days = list()
for i in range(n):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        n_days.append(j)
for i in range(m):
    start, end = map(int, input().split())
    for j in range(start, end + 1):
        m_days.append(j)
n_days.sort()
m_days.sort()
days_work_together = 0
for day in n_days:
    if day in m_days:
        days_work_together += 1
# print(n_days)
# print(m_days)
print(days_work_together)
