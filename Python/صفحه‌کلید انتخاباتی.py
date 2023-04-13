n = int(input())
caps = 0
word = ""
for i in range(n):
    char = input()
    if char == "CAPS":
        caps += 1
        caps %= 2
        continue
    if caps == 1:
        # print("here")
        char = char.upper()
    word += char

print(word)
