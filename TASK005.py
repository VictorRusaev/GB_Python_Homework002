# 5'. Реализуйте алгоритм перемешивания списка.
# Например, сортировка по убыванию:

import random
newList = []
for i in range(10):
    newList.append(random.randint(-10, 10))
print(newList)

for i in range(len(newList) - 1):
    for j in range(len(newList) - i - 1):
        if newList[j + 1] > newList[j]:
            bufer = newList[j]
            newList[j] = newList[j + 1]
            newList[j + 1] = bufer
print (newList)