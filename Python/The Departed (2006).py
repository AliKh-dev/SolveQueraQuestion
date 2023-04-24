jets = []
for i in range(5):
    registration_code = input()
    if "FBI" in registration_code:
        jets.append(i + 1)
if len(jets) > 0:
    print(*jets)
else:
    print("HE GOT AWAY!")
