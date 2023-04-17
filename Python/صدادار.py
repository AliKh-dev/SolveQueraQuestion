string = input()
vowels = ['a', 'e', 'i', 'o', 'u']
cnt_vowels = 0
for letter in string:
    if letter in vowels:
        cnt_vowels += 1
print(cnt_vowels)
