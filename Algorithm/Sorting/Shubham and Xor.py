'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n =int(input())
arr = [int(i) for i in input().split()]
temp=[]
k =0
import collections
c=collections.Counter(arr)
for i,j in dict(c).items():
        su = (j-1)*j/2
        k = k+su
        
print(int(k))
