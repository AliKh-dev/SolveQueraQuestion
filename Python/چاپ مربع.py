n = int(input())
print(n * "*")
for i in range(n-2):
    string = (n-2) * " "
    print(f"*{string}*")
print(n * "*")
