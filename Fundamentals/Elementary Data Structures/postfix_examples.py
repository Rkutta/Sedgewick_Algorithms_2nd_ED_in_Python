'''
Algorithms 2nd. Ed by Robert Sedgewick
Chapter 3: Elementary Data Structures pg 28
Program: postfix_examples (part 1)
Implemented in Python by Edward Heronzy
'''
import pushdown_stack

pushdown_stack.stackinit()
c = True
expression = ''
while c:
    c = input()
    if c == ')':
        expression += pushdown_stack.pop()
    if c == '+':
        pushdown_stack.push(c)
    if c == '*':
        pushdown_stack.push(c)
    if (c > '0') and (c <= '9'):
        expression += c
    if c != '(':
        expression += ' '
print(expression)