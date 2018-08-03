'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    z,a,b=map(int,input().split())
    k = round(b*z/(a+b))
    t = a*(k**2)+b*((z-k)**2)
    print(t)
