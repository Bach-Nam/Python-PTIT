def is_valid():
    if len(path) >= 3 and path[-3] == 1 and path[-2] == 0 and path[-1] == 1:
        return False
    return True
def backTrack():
    if len(path) == n:
        print(*path)
        return
    for bit in (0,1):
        path.append(bit)
        if is_valid():
            backTrack()
        path.pop()
n = int(input())
path = []
backTrack()