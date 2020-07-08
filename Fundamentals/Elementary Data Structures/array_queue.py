'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 30
Program: array_queue
Implemented in Python by Edward Heronzy
'''
max = 100
queue = [int()] * 100

def put(v):
    queue[tail] = v
    tail += 1
    if tail >= max:
        tail = 0

def get():
    g = queue[head]
    head += 1
    if head >= max:
        head = 0
    return g

def queueinitialize():
    global head
    global tail
    head = 0
    tail = 0

def queueempty():
    return head == tail