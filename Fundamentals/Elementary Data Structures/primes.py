'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Data Structures pg 16
Program: primes
Implemented in Python by Edward Heronzy
'''
# Since Python does not have a built-in array data structure,
# I have pre-initialized a list to the array's max-length
# to replicate it
N = 1000
a = [bool] * (N+1)
a[0] = False
a[1] = False
for i in range(2,N):
    a[i] = True
for i in range(2,int((N+1)/2)):
    for j in range(2,int((N+1)/i)):
        a[i*j] = False
for i in range(0,N):
    if a[i]:
        print(i)
