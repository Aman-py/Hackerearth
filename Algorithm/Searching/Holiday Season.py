'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
s = input()
k=0
for i in range(n-3):
    if s[i]==s[i+2] and s[i+1] == s[i+3]:
        k+=1
print(k)
