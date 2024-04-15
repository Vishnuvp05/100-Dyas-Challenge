def convertion(s):
    if s[-2:]=='AM':
        if s[:2]=='12':
            return '00'+s[2:-2]
        else:
            return s[:-2]
    else:
        h=int(s[:2])
        if h<12:
            h+=12
        return str(h)+s[2:-2]
    
a='12:05:45 AM'
c='07:04:50 PM'
b=convertion(a)
d=convertion(c)
print(b)
print(d)