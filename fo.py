#!/usr/bin/python
sum = 0
for x in range(101):
    sum = sum +x
print sum

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

sum  = 0
n = 1
while n < 100:
    sum = sum + n
    n = n + 2
print sum

age = raw_input('age:')
if age < 2000:
    print u'00 front'
else:
    print u'00 after'

def my_abs(x):
    if not isinstance(x, (int, float)):
            raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

my_abs("A")
