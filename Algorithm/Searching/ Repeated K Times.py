n = int(input())
arr = [int(i) for i in input().split(' ')]
k = int(input())
while True:
    if arr.count(min(arr)) == k:
        print(min(arr))
        break
    else:
        arr.remove(min(arr))




#imported code
import collections
n=int(input())
lst=list(map(int,input().split(" ")))
p=int(input())
c=collections.Counter(lst)
for i,j in dict(c).items():
    if j==p:
        print (i)
        break
