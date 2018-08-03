'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n = 0
while n<2000:
    k = input()
    if "->" in k:
        print(k.replace("->","."))
        n-=1
    else:
        print(k)
        n-=1
