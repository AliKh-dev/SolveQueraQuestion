x1 = int(input())
v1 = int(input())
x2 = int(input())
v2 = int(input())
delta_v = v2 - v1
delta_x = x2 - x1
if delta_v == 0:
    print("WAIT WAIT")
elif delta_v * delta_x > 0:
    print("BORO BORO")
elif delta_v * delta_x < 0:
    print("SEE YOU")
