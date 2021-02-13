import sys

while True:
    tmp = sys.stdin.readline()
    if tmp == '.\n':
        break
    bracket = []
    for i in tmp:
        if i == '(' or i == '[':
            bracket.append(i)
        elif i == ')':
            if not bracket or bracket.pop() != '(':
                print('no')
                break
        elif i == ']':
            if not bracket or bracket.pop() != '[':
                print('no')
                break
    else:
        print('yes') if not bracket else print('no')
