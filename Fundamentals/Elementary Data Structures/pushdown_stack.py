'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 27
Program: pushdown_stack
Implemented in Python by Edward Heronzy
'''
class node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

def stackinit():
    global head
    global z
    head = node()
    z = node()
    head.next = z
    z.next = z
    
def push(v):
    t = node()
    t.key = v
    t.next = head.next
    head.next = t
    
def pop():
    t = head.next
    pop = t.key
    head.next = t.next
    del t
    return pop

def stackempty():
    stackempty = (head.next == z)
    return stackempty