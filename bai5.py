# def backtrack(start):
#     if len(combo) == k:
#         print(' '.join(map(str, combo)))   # in luôn, khỏi lưu vào đâu cả
#         return
#     for num in range(start, limit + 1):
#         combo.append(num)
#         backtrack(num + 1)
#         combo.pop()

# n, k, x = map(int, input().split())
# limit = min(n, x - 1)
# combo = []
# backtrack(1)






def backTrack(start):
    if len(combo) == k:
        print(' '.join(map(str,combo)))
        return
    for num in range(start, limit+1):
        combo.append(num)
        backTrack(num + 1)
        combo.pop()
n,k,x = map(int, input().split())
limit = min(n, x-1)
combo = []
backTrack(1)
