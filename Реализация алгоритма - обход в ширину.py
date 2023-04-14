a = list(map(int, input().split()))
b = []
stack = [0]
visited = []

for i in range(a[1]):
    b.append(list(map(int, input().split())))

def func_1(stack, visited, b, d, n):
    if n == 0:
        return 0
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
            if b_1[j][0] == stack_1[i]:
                stack.append(b_1[j][1])
            if b_1[j][1] == stack_1[i]:
                stack.append(b_1[j][0])
    visited = visited + stack_1
    d += 1
    for i in range(len(stack)):
        if n == stack[i]:
            return d
    return func_1(stack, visited, b_1, d, n)

print('Дан связный, неориентрированый, невзвешенный граф:')
for i in range(a[0]):
    print(f'Минимальное расстояное от 0-ой вершины, до {i} -', func_1(stack, visited, b, 0, i))