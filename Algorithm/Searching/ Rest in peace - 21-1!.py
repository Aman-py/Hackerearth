'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = int(input())
for i in range(n):
    t = input()
    if '21' in t or int(t)%21==0:
        print('The streak is broken!')
    else:
        print('The streak lives still in our heart!')
