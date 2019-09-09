#! /usr/bin/env python3
import sys

def answer(x,y):
        z = abs(x-y)
        return z

def solve():
    for line in sys.stdin:
        xy = line.split()
        x = int(xy[0])
        y = int(xy[1])
        print(answer(x,y))

def test():
    assert answer(4,4) == 0
    assert answer(6,9) == 3
    print('all test cases passed...')

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
