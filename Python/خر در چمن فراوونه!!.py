a, b, l = input().split()
a = int(a)
b = int(b)
l = int(l)
k = 0
sum = 0
while k < l:
    sum += a
    k += 1
    if k == l:
        break
    sum += b
    k += 1
print(sum)
