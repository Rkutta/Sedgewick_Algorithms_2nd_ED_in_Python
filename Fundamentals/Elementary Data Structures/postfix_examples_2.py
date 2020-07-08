'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 28
Program: postfix_examples (part 2)
Implemented in Python by Edward Heronzy
'''
import pushdown_stack
pushdown_stack.stackinit()
x = 0
c = input()
while c:
    if c == '*':
        x = pushdown_stack.pop() * pushdown_stack.pop()
    if c == '+':
        x = pushdown_stack.pop() + pushdown_stack.pop()
    if (c >= '0') and (c <= '9'):
        x = int(c)
    pushdown_stack.push(x)
    c = input()
print(pushdown_stack.pop())
        