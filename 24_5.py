s = open('24 (2).txt').readline()
m = 10000
for l in range(len(s)):
    for r in range(l+m,l,-1):
        c = s[l:r+1]
        if c.count('QFG')<105:break
        elif c.count('QFG')==105 and c[0]!='Q':
            m = min(m,len(c))
print(m)