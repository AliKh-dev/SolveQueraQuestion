n, l = map(int, input().split())
time_spend = 0
distance_travel = 0
for i in range(n):
    distance, red, green = map(int, input().split())
    time_spend += (distance - distance_travel)
    distance_travel += (distance - distance_travel)
    if time_spend % (red + green) < red:
        time_spend += (red - time_spend % (red + green))
    # print(f"Distance travel: {distance_travel}")
    # print(f"Time spend: {time_spend}")
    # print("----------------")
time_spend += (l - distance_travel )
print(time_spend)
