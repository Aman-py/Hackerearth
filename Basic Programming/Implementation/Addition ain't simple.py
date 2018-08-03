t = int(input())
for i in range(t):
    s = input()
    n = len(s)
    l = n-1
    q = ''
    for i in range(n):
        k = ord(s[i])+ord(s[l-i])
        m = (k%97)+98
        if m > 122:
            m = m%123
            q = q+chr(m+97)
        else:
            q = q+chr(m)
    print(q)
