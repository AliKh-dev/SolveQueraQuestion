n = int(input())
temps = [int(i) for i in input().split()]
for i in range(n):
    if temps[i] > 15:
        print("cooler")
    else:
        print("heater")
