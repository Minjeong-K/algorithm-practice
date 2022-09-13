'''
https://www.acmicpc.net/problem/2884
'''

h, m = list(map(int, input().split()))[:2]
m -= 45

if m < 0:
    m += 60
    h -= 1
    if h < 0:
        h += 24

print(h, m)