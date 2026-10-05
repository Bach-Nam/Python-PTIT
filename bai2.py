n = int(input())
for i in range( 2**n):
    k = i ^ (i >> 1)
    print(format(k,f'0{n}b'))