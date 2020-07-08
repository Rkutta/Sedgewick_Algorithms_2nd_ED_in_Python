'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 23
Program: linked_lists_as_arrays
Implemented in Python by Edward Heronzy
'''
N = 1000
key = [int()] * 1000
next = [int()] * 1000
def listinitialize(): 
    global head
    global x
    global z       
    head = 0
    z = 1
    x = 1
    next[head] = z
    next[z] = z

def deletenext(t):
    next[t] = next[next[t]]
    
def insertafter(v, t):
    global x
    x = x + 1    
    key[x] = v
    next[x] = next[t]
    next[t] = x
    

