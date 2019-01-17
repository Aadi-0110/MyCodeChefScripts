array = {
0:0,
1:1
}

def solve(n):
    if n in array:
        return array[n]
    else:
        array[n] = max(n,solve(n//2)+solve(n//3)+solve(n//4))
        return array[n]

if __name__ == '__main__':
    i = 10
    while(i > 0):
        n = int(input())
        print(solve(n))
        i -= 1
