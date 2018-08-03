'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
arr = [int(i) for i in input().split()]
q = int(input())
for i in range(q):
    t = int(input())
    m = [-1]
    for k in range(1,len(arr)+1):
        if sum(arr[:k])>=t:
            m.append(k)
            break
    print(m[-1])
