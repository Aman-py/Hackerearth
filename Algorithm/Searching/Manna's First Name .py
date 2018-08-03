'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
for i in range(t):
    n = input()
    k = n.split('SUVOJIT')
    m = len(k)-1
    l = 0
    for j in k:
        x=j.split('SUVO')
        l =l+(len(x)-1)
    print('SUVO = '+str(l)+','+' SUVOJIT = '+str(m))
