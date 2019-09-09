#! /usr/bin/env python3
import sys

def answer(board_size):
        if int(board_size) == 1:
                return 1
        else:
                return (int(board_size) * 2 - 2)

def solve():
    lines = sys.stdin
    for line in lines:
            print(answer(line))          

def test():
    assert answer(1) == 1
    assert answer(20) == 38
    assert answer(1000) == 1998
    print('all test cases passed...')

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
