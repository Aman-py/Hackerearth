'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t = int(input())
g = {}
m = {}
for i in range(1,t+1):
    n = input()
    if n[0] == 'G':
        for s in n.split(' '):
            if s.isdigit():
                if s in g:
                    g[s]+=2
                else:
                    g[s]=2
    elif n[0] == 'M':
        for s in n.split(' '):
            if s.isdigit():
                if s in m:
                    m[s]+=1
                else:
                    m[s]=1
if g['19']>m['19'] or g['20'] >m['20']:
    print('Date')
else:
    print('No Date')
            
