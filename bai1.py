n,k = map(int,input().split())
if 1<k<n:
    for i in range(n-k, -1,-1):
        print("0" * i + "1" * k + "0" *(n-i-k))


