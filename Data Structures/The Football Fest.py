'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
for i in range(n):
    m,d = [int(i) for i in input().split()]
    x =[]
    y =[]
    for i in range(m):
        op = [i for i in input().split()]
        if op[0] == 'P':
            x.append(op[0])
            y.append(op[1])
        elif op[0] == 'B':
            temp = y[-1]
            y[-1]=y[-2]
            y[-2]=temp
    print('Player',y[-1])
            
    
