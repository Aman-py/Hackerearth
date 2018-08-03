'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def ror(arr):
    n = len(arr)
    arr=arr[n-1:]+arr[:n-1]
    return arr
n,r,c = map(int,input().split())
arr = []
for i in range(n):
    k = [int(i) for i in input().split()]
    arr.append(k)
r = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
for p in r:
    arr[p-1]=ror(arr[p-1])
for q in c:
    for j in range(n):
        arr[j][q-1],arr[n-1][q-1] = arr[n-1][q-1],arr[j][q-1]
for x in range(n):
    print(' '.join(str(i) for i in arr[x]))
