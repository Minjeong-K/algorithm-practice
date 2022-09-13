'''
https://www.acmicpc.net/problem/1712
'''

a, b, c = list(map(int, input().split()))

if b >= c:
    print(-1)
else:
    n = a // (c-b) + 1
    print(n)