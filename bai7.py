def backTrack(start):
    if len(path) == k:
        print(*path)
        return
    for num in range(start,n+1):
        path.append(num)
        backTrack(num + 1)
        path.pop()
n, k = map(int,input().split())
path =[]
backTrack(1)