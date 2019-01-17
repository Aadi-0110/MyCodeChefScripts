"""
Link: https://www.codechef.com/problems/FCTRL2
Question: You are asked to calculate factorials of some small positive integers.

Input: An integer t, 1<=t<=100, denoting the number of test cases, followed by t lines, each containing a single
integer n, 1<=n<=100.

Output: For each integer n given at input, display a line with the value of n!
"""

N = int(input())
t = []
for i in range(N):
    t.append(int(input()))

max_term = max(t)
k = 1
fact = [1]
for i in range(1, max_term+1):
    k *= i
    fact.append(k)

for i in t:
    print(fact[i])
