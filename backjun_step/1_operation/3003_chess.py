'''
https://www.acmicpc.net/problem/3003
'''

black_list = [1, 1, 2, 2, 2, 8]    # king, queen, rook, bishop, knight, pawn

white = input()
white_list = white.split()

for b, w in zip(black_list, white_list):
    print(str(b-int(w)), end=' ')
