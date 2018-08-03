import numpy as np
n = int(input())
a=list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
c = set(np.array(b)-a[0])
for i in range(1,n):
    c = c&set(np.array(b)-a[i])
if len(c) > 100:
    print(' '.join(str(i) for i in c[:100]))
else:
    print(' '.join(str(i) for i in c))
