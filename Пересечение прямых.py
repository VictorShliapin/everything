#Необходимо найти точку пересечения двух прямых на плоскости, если она существует.

first = list(map(int, input().split()))
second = list(map(int, input().split()))
a_1, b_1, c_1 = first[0], first[1], first[2]
a_2, b_2, c_2 = second[0], second[1], second[2]

if b_2*a_1 == b_1*a_2:
    print('NO')
else:
    x = ((b_1*c_2 - b_2*c_1)/(b_2*a_1 - b_1*a_2))
    y = (-(c_2 + a_2*x)/b_2)
    print(round(x), round(y))

