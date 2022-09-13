'''
https://www.acmicpc.net/problem/25304
'''

total = int(input())
n = int(input())
buy = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    buy += a*b

if buy == total:
    print('Yes')
else:
    print('No')