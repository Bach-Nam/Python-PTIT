def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def backtrack(start, n, k, path):
    if len(path) == k:
        if is_prime(sum(path)):
            print(' '.join(map(str, path)))
        return
    for num in range(start, n + 1):
        path.append(num)
        backtrack(num + 1, n, k, path)
        path.pop()

n, k = map(int, input().split())
backtrack(1, n, k, [])

