a = int(input())
b = int(input())
c = int(input())
if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if c ** 2 + b ** 2 == a ** 2:
    print("YES")
else:
    print("NO")