row, column = input().split()
row = int(row)
column = int(column)
if column <= 10:
    right = True
    k = column
else:
    right = False
    k = (20-column)+1
a = (10-row)+1
if right:
    print('Right', a, k)
else:
    print('Left', a, k)
