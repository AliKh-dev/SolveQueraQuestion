left1,  right1 = input().split()
left2,  right2 = input().split()
if left1 == right1 or left1 == right2 or right1 == left2 or left2 == right2:
    print("YES")
else:
    print("NO")
