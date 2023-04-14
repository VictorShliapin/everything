a = int(input())
a_1 = int(input())
b = []
for i in range(a_1):

    b.append(list(map(int, input().split())))

def func(stack, visited, b):
    stack_1 = stack[-1]
    stack_2 = stack.copy()
    b_1 = b
    for i in range(len(b_1)):
        if b_1[i][0] == stack_1 and b_1[i][1] not in visited:
            stack.append(b_1[i][1])
            break
        if b_1[i][1] == stack_1 and b_1[i][0] not in visited:
            stack.append(b_1[i][0])
            break
    if stack_1 not in visited:
        visited = visited + [stack_1]
    if stack == stack_2:
        stack = stack[:-1]
    if stack == []:
        return visited
    return func(stack, visited, b_1)

res = [sorted(func([x], [], b)) for x in range(a)]
s = {}
def func_1(res, a):
    d = 0
    for i in range(len(res)):
        if a == res[i]:
            d += 1
    return d

for i in range(len(res)):
    s[res[i]] = func_1(res, res[i])


print(s)