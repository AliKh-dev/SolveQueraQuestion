number1 = int(input())
number2 = int(input())

while True:
    if number1 % number2 == 0:
        break
    number1, number2 = number2, number1 % number2

print(number2)