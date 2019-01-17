def solve(n,k):
    e=1
    if n == k:
      return 1
    if n<k:
      return 0
    if n>k :
        for i in range(min(k-1,n-k)):
           n -= 1
           e=(e*n)//(i+1)

    return e

T = int(input())
for i in range(T):
    n, k= [int(x) for x in input().split()]
    print(solve(n,k))