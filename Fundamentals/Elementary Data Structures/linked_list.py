'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 20
Program: linked_list
Implemented in Python by Edward Heronzy
'''
# Single Linked List
class node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next

def listinitialize():
    global head
    global z
    head = node()
    z = node()
    head.next = z
    z.next = z

def deletenext(t):
    t.next = t.next.next
    
def insertafter(v,t):
    x = node()
    x.key = v
    x.next = t.next
    t.next = x
    
''' 
Author's Note:

To eleborate on a bit of confusion that may
arise when comparing the Pascal code to the
Python implementation, Python does not implement
pointers. You cannot initialize a pointer type in
Python (as it goes against the philosophy of Python
that simple is better than complex). But if you look
at how objects are created in Python, you can see
that each variable we create is in itself a pointer
to a PyObject in memory which has a type, value, and
reference count. So think of the "head" and "z" variables 
as pointing to a node() object in memory that we can access
and change through these variables. But do not call
them "pointers" because they are not the same as those 
found in Pascal or C++. Call them "variables"
'''