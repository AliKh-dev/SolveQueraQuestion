word = input()
cnt = 1
for letter in word:
    if letter == 'R':
        cnt *= 3
    elif letter == "L" or letter == "F" or letter == "G" or letter == "D" or letter == "T":
        cnt *= 2

print(cnt)