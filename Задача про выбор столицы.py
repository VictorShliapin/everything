#Некоторые из городов государства соединены дорогами.
# Жители этого государства просят вас помочь им с выбором столицы: требуется, чтобы сумма расстояний
# от столицы до каждого из остальных городов была минимальна.
#Для удобства города уже пронумерованы от 0 до n-1 .
#Формат входных данных
#На вход программе в первой строке подается два числа через пробел: n и m .
#•	2 ≤ n ≤ 100 - число городов
#•	1 ≤ m ≤ 500 - число дорог
#В следующих m строках задаются дороги. Дорога задаётся тремя числами - два номера соединенных дорогой городов и длина дороги.
#Формат выходных данных
#Выведите номер столицы. Если возможно несколько вариантов, то вывести номер столицы с минимальным номером.

import math
inf = math.inf

a = list(map(int, input().split()))
b = []
res_1 = []
for i in range(a[1]):
    b.append(list(map(int, input().split())))


def func_1(stack, visited, b, peak):
    stack_1 = stack.copy()
    stack = []
    b_1 = []
    for j in range(len(b)):
        if b[j][0] not in visited and b[j][1] not in visited:
            b_1.append(b[j])
    if visited == []:
        b_1 = b
    for i in range(len(stack_1)):
        for j in range(len(b_1)):
            if b_1[j][0] == stack_1[i] and b_1[j][1] not in stack:
                stack.append(b_1[j][1])
            if b_1[j][1] == stack_1[i] and b_1[j][0] not in stack:
                stack.append(b_1[j][0])
            if b_1[j][0] == stack_1[i] and b_1[j][2]+peak[stack_1[i]][1] < peak[b_1[j][1]][1]:
                peak[b_1[j][1]][1] = b_1[j][2]+peak[stack_1[i]][1]
                peak[b_1[j][1]][2] = peak[b_1[j][0]][2] + 1
            if b_1[j][1] == stack_1[i] and b_1[j][2]+peak[stack_1[i]][1] < peak[b_1[j][0]][1]:
                peak[b_1[j][0]][1] = b_1[j][2]+peak[stack_1[i]][1]
                peak[b_1[j][0]][2] = peak[b_1[j][1]][2] + 1
    visited = visited + stack_1
    if b_1 == []:
        return peak
    return func_1(stack, visited, b_1, peak)

for s in range(a[0]):
    peak = [[x, inf, inf] for x in range(a[0])]
    for i in range(len(peak)):
        if peak[i][0] == s:
            peak[i][1] = 0
            peak[i][2] = 1
    res = 0
    for j in range(a[0]):
        res += func_1([s], [], b, peak)[j][1]
    res_1.append(res)

for i in range(len(res_1)):
    if res_1[i] == min(res_1):
        print(i)
        break