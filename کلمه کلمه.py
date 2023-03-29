vowels = ['a','e','u','i','o']
word = input()
cnt = 1
for letter in word:
    if letter in vowels:
        cnt *= 2
print(cnt)