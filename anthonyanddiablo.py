#! /usr/bin/env python3
import sys
from math import pi

def answer(A,N):
    radian = N / (2*pi)
    area = pi * (radian**2)
    if area >= A:
        return 'Diablo is happy!'
    else:
        return 'Need more materials!'

def solve():
    A, N, = map(float, input().split())
    print(answer(A,N))

def test():
    assert answer(5.000000, 0.000000) == 'Need more materials!'
    assert answer(1.000000, 8.000000) == 'Diablo is happy!'
    print("all test cases passed...")

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()