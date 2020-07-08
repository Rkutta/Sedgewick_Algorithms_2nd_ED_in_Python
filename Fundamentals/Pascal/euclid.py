'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 2: Pascal pg 8
Program: euclid
Implemented in Python by Edward Heronzy
'''

def gcd(u, v):
    while u != 0:
        t = 0
        if u < v:
            t = u
            u = v
            v = t
        u = u - v
    return v

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print(gcd(x,y))