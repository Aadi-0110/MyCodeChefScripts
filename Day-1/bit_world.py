N = int(input())
t = []
"""
0    0    8
1    0    0
0    1    0
0    0    1
2    0    0
"""


def solve(n):
    if n == 0:
        return 1,0,0
    z = int(n/26)
    e = n % 26
    if 1 <= e <= 2:
        return 2**z, 0, 0
    elif 3 <= e <= 10:
        return 0, 2**z, 0
    elif 11 <= e <= 27 or e == 0:
        if e == 0:
            return 0, 0, 2 ** (z-1)
        return 0, 0, 2 ** z


for i in range(N):
    t.append(solve(int(input())))

for i in t:
    w,x,y = i
    print(w,x,y)
