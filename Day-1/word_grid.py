"""
Link:
https://www.codechef.com/problems/WORDGRID
"""
from typing import List, Any

T = int(input())
words = []
for i in range(T):
    N = int(input())
    k = []
    for j in range(N):
        k.append(input())
    words.append(k)

for word in words:
    j = []
    for i in word:
        l: List[Any] = list(i)
        for e in l:
            if e not in j:
                j.append(e)
    if len(j) > 16:
        print("grid\nsnot\nposs\nible")
    else:
        w = "".join(j)
        print(w[0:4], w[4:8], w[8:12], w[12:16], sep="\n")
