number1 = abs(int(input()))
number2 = abs(int(input()))
if number1 == 0:
    print(number2)
    quit()
elif number2 == 0:
    print(number1)
    quit()
if number2 > number1:
    number1, number2 = number2, number1

while True:
    if number1 % number2 == 0:
        break
    number1, number2 = number2, number1 % number2

print(number2)