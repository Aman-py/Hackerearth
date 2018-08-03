n,m = [int(i) for i in input().split()]
arr = [int(i) for i in input().split()]
j =[]
for i in range(len(arr)-1,0,-1):
    if arr[i] == m:
        j.append(i+1)
        break
if j[-1]==0:
    print(-1)
else:
    print(j[-1])
