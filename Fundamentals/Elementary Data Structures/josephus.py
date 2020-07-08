'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 22
Program: josephus
Implemented in Python by Edward Heronzy
'''
# Utilizes Circular Linked List
class node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

N = int(input())
M = int(input())
t = node()
x = node()
t.key = 0
x = t

for i in range(1,N):
    t.next = node()
    t = t.next
    t.key = i
t.next = x

while t != t.next:
    for i in range(0, M-1):
        t = t.next
    print(t.next.key + 1)
    x = t.next
    t.next = t.next.next
    del x

print(t.key + 1)