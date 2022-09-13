'''
https://www.acmicpc.net/problem/2525
'''

a, b = list(map(int, input().split()))[:2]
c = int(input())

c_h, c_m = c // 60, c % 60

a += c_h
b += c_m

if b >= 60:
    b -= 60
    a += 1
if a >= 24:
    a -= 24

print(a, b)
