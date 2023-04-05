word = list(input())
len_word = len(word)
i = 0
while i < len_word:
    if i != 0:
        if word[i] == '=':
            word.pop(i - 1)
            word.pop(i - 1)
            i -= 2
            len_word -= 2
    else:
        if word[i] == '=':
            word.pop(i)
            i -= 1
            len_word -= 1
    i += 1
print("".join(word))
