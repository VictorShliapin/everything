import math
inf = math.inf

a = list(map(int, input().split()))
s = a[2] #start
f = a[3] #finish
b = []
stack = [0]
visited = []
peak = [[x, inf, inf] for x in range(a[0])]
for i in range(a[1]):
    b.append(list(map(int, input().split())))
for i in range(len(peak)):
    if peak[i][0] == s:
        peak[i][1] = 0
        peak[i][2] = 1

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
print('Алгоритм возвращает список из списков, в каждом из которых:')
print('1-ый эл. это вершина')
print(f'2-ой это вес минимального пути до данной вержины от {s}')
print('3-ий - это кол-во вершин которое было пройдено на пути')
print(func_1([s], [], b, peak))
