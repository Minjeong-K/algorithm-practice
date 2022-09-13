'''
https://www.acmicpc.net/problem/2753
'''

def is_leafyear(y):
    if year % 4 == 0:
        if year % 100 != 0:
            return 1
        elif year % 400 == 0:
            return 1
    return 0

year = int(input())

print(is_leafyear(year))