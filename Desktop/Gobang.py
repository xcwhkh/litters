#coding:utf-8
import os

# ---initialize---
p=[['.' for j in range(21)] for i in range(21)]
turn = 1
title = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

def pprint():
    os.system('cls')
    print(' ', end = '')
    for i in range(16):
        print('%2c' % title[i], end = '')
    print()
    for i in range(16):
        print('%c ' % title[i], end = '')
        for j in range(16):
            print(p[i][j],'', end = '')
        print()

def judge(x, y):
    num = 1
    i = 1
    while p[x-i][y] == p[x][y]:
        num = num + 1
        i = i + 1
    i = 1
    while p[x+i][y] == p[x][y]:
        num = num + 1
        i = i + 1
    if num >= 5:
        return True

    num = 1
    i = 1
    while p[x][y-i] == p[x][y]:
        num = num + 1
        i = i + 1
    i = 1
    while p[x][y+i] == p[x][y]:
        num = num + 1
        i = i + 1
    if num >= 5:
        return True

    num = 1
    i = 1
    while p[x-i][y-i] == p[x][y]:
        num = num + 1
        i = i + 1
    i = 1
    while p[x+i][y+i] == p[x][y]:
        num = num + 1
        i = i + 1
    if num >= 5:
        return True

    num = 1
    i = 1
    while p[x+i][y-i] == p[x][y]:
        num = num + 1
        i = i + 1
    i = 1
    while p[x-i][y+i] == p[x][y]:
        num = num + 1
        i = i + 1
    if num >= 5:
        return True

    return False

def trans(a):
    x = ord(a)
    if x >= 97 :
        x = x - 87
    else :
        x = x - 48
    return x

# -----play-----
while(True):
    pprint()
    if turn == 1:
        act = input('black turn:').split()
        x = trans(act[0])
        y = trans(act[1])
        if 0<=x<=16 and 0<=y<=16 and p[x][y] == '.':
            p[x][y] = 'X'
            turn = 0
        else:
            print('error')
            os.system('pause')
            continue
    else:
        act = input('white turn:').split()
        x = trans(act[0])
        y = trans(act[1])
        if 0<=x<=16 and 0<=y<=16 and p[x][y] == '.':
            p[x][y] = 'O'
            turn = 1
        else:
            print('error')
            os.system('pause')
            continue
    if(judge(x,y)):
        pprint()
        if turn == 0:
            print('black win')
        else:
            print('white win')
        break
