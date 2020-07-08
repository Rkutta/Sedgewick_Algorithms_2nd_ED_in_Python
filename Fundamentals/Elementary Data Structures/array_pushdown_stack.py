'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 29
Program: array_pushdown_stack
Implemented in Python by Edward Heronzy
'''
maxP = 100
stack = [int()] * maxP

def push(v):
    stack[p] = v
    p += 1

def pop():
    p -= 1
    return stack[p]

def stackinit():
    global p
    p = 0

def stackempty():
    return p <= 0