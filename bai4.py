def backTrack(start,n,k,target,path,target_num):
    if target_num > target:
        return
    if len(path) == k:
        if target_num == target:
            print(' '.join(map(str,path)))
        return
    for num in range(start, n+1):
        path.append(num)
        backTrack(start+1, n,k,target,path, target_num +num )
        path.pop()
n,k,target = map(int, input().split())
backTrack(1,n,k,target,[], 0)
