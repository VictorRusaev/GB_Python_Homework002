# 4'. Задайте список из N элементов, заполненных числами 
# из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
# -2 -1 0 1 2
# Позиции: 0,1 -> 2

# with open('a.txt', 'r') as f:
#     a = f.read().split(' ')
# print(a)

n = int(input('N = '))
list = []
for i in range(-n,n+1):
    list.append(i)
    print(f' {i} ', end=' ')
print()

elements = input(f'Элементы от 0 до {len(list) - 1} через пробел: ').split()
mult = 1
for i in range(0, len(elements)):
    mult = mult * list[int(elements[i])]
print(f'Произведение элементов равно: {mult}')
