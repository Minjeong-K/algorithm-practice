'''
https://www.acmicpc.net/problem/1330
'''

A, B = list(map(int, input().split()[:2]))

if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
