n, m = map(int, input().split())
conversation = dict()
for i in range(n):
    goat, barber = input().split()
    conversation[goat] = barber + " kachal!"
goat = input().split()
for word in goat:
    if word in conversation.keys():
        print(conversation[word], end=" ")
    else:
        print("kachal!", end=" ")
