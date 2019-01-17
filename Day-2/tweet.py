# Taking the inputs
N,K = [int(x) for x in input().split()]

# intializing the main list to store the status of tweet
arr = [0]*N
for i in range(K):
    e = input()
    if e != 'CLOSEALL':
        com, pos = [x for x in e.split()]
        if arr[int(pos) - 1] == 1:
            arr[int(pos)-1] = 0
        else:
            arr[int(pos)-1] = 1
    else:
        arr = [0]*N
    print(arr.count(1))

