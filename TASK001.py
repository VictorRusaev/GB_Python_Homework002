# 1'. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# - 6782 -> 23
# - 0,56 -> 11

n = float(input('Введите вещественое число: '))
nStr = str(n)
sum = 0
for i in range(len(nStr)):
    if nStr[i] != '.':
        sum = sum + int(nStr[i])
print(sum)