word = input()
cnt = 1
for letter in word:
    if letter == "L" or letter == "F"  or letter == "D" or letter == "T":
        cnt *= 2

print(cnt)