# 3'. Задайте список из n чисел последовательности (1+1/n)^n 
# и выведите на экран их сумму.

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 
# 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('n = '))
newList = []
for i in range(1, n+1):
    newList.append((1 + 1/i) ** i)
print(newList)
sum = 0
for i in range(len(newList)):
    sum = sum + newList[i]
print(sum)