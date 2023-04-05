watermelons = [int(i) for i in input().split()]
cnt_Satisfaction = 0
for i in range(5):
    if watermelons[i] >= 80:
        cnt_Satisfaction += 1
if cnt_Satisfaction >= 3:
    print("Mamma mia!")
elif 1 <= cnt_Satisfaction <= 2:
    print("Mamma mia!!")
else:
    print("Mamma mia!!!")
