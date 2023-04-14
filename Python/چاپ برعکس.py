i = 0
found = []
while True:
    found.append(input())
    if int(found[-1]) == 0:
        found.pop()
        break
for i in range(len(found)-1,-1,-1):
    print(found[i])
