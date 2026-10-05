def solve(n,k):
    path = []
    def backTrack(start):
        if len(path) == k:
            print(*path)
            return 
        for num in range(start, n+1):
            path.append(num)
            backTrack(num + 2)
            path.pop()
    backTrack(1)
n, k = map(int,input().split())
solve(n,k)