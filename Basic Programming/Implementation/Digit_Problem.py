'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n,k = map(int,input().split())
n = list(str(n))
count = 0
lenth = len(n)
for i in range(lenth):
    if n[i] = '9' and count<k:
        n[i] = '9'
        count+=1
print(''.join(n))
