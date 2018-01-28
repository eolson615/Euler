total = 0
number1 = 1
number2 = 1
while number2 < 4000000:
    if number2 % 2 == 0:
        total += number2
    numberF = number1 + number2
    number1 = number2
    number2 = numberF
print(total)
