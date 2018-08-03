'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
arr = [int(i) for i in input().split()]
l = set(arr)
k = 0
for i in range(n):
    print(i)
    for j in range(n):
        if set(arr[i:j]) == l:
            k=k+(n-j)
            break
print(k)
