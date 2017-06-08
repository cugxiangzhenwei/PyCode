#!/usr/bin/python
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 1
print L

L = ['adam', 'LISA', 'barT']
def tu(s):
    return s.upper()

def tl(s):
    return s.lower()

def pro_text(s):
    str  = tu(s[0:1]) + tl(s[1:])
    return str

l = map(pro_text,L)
print l


