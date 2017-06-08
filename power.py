#!/usr/bin/python
def power(x, n=2):

    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print power(5, 3)
print power(9)
print power(4,3)
