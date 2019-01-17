N = int(input())
t = []


def solve(i):
    x = [int(k) for k in list(i)]
    return sum(x)


for i in range(N):
    print(solve(input()))


