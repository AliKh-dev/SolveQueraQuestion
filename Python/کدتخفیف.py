n, primary = input().split()
primary = sorted(set(primary))
n = int(n)
results = [""] * n
for code in range(n):
    if sorted(set(input())) == primary:
        results[code] = "Yes"
        continue
    results[code] = "No"
for result in results:
    print(result)