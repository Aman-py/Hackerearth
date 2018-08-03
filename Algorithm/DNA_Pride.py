def check(s):
    k = len(s)
    ss = [0]*k
    if 'U' in s:
        return 'Error RNA nucleobases found!'
    for i in range(k):
        if s[i] =='T':
            ss[i]='A'
        elif s[i]=='A':
            ss[i]='T'
        elif s[i] == 'G':
            ss[i]='C'
        elif s[i] == 'C':
            ss[i]='G'
    return ''.join(k for k in ss)
t = int(input())
for i in range(t):
    s = input()
    print(check(s))
