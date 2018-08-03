from sys import stdin
def countsetbits(n):
    count = 0
    while n:
        count += n&1
        n >>= 1
        if count == 2:
            return True
    return False
t= int(stdin.readline())
for i in range(t):
    n = int(stdin.readline())
    l = 0
    for i in range(1,n+1):
        if countsetbits(i):
            l+=i
    print(l%1000000007)
