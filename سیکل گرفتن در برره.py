n = int(input())
results = input()

keyvan = [3, 3, 1, 1, 2, 2]
keyvan_score = ["keyvoon", 0]

nezam = [1, 2, 3]
nezam_score = ["nezam", 0]

shir_farhad = [2, 1, 2, 3]
shir_farhad_score = ["shir farhad", 0]

for i in range(n):
    if int(results[i]) == keyvan[i % len(keyvan)]:
        keyvan_score[1] += 1
    if int(results[i]) == nezam[i % len(nezam)]:
        nezam_score[1] += 1
    if int(results[i]) == shir_farhad[i % len(shir_farhad)]:
        shir_farhad_score[1] += 1
print(max(shir_farhad_score[1], nezam_score[1], keyvan_score[1]))

if keyvan_score[1] == max(shir_farhad_score[1], nezam_score[1], keyvan_score[1]):
    print(keyvan_score[0])
if nezam_score[1] == max(shir_farhad_score[1], nezam_score[1], keyvan_score[1]):
    print(nezam_score[0])
if shir_farhad_score[1] == max(shir_farhad_score[1], nezam_score[1], keyvan_score[1]):
    print(shir_farhad_score[0])
