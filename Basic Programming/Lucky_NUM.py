'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from sys import stdin
t = int(stdin.readline())
for j in range(t):
    n = int(stdin.readline())
    l =0
    for i in range(1,n+1):
        k = bin(i)
        if k.count('1') == 2:
            l = l+i
    print(l)
