#! /usr/bin/env python3
import sys

def answer(prices):
    maxdiscount = 0
    for i in range(2, len(prices), 3):
        maxdiscount += prices[i]
    return maxdiscount

def solve():
    numitems = int(input())
    prices = sorted(map(int, input().split()), reverse=True)
    print(answer(prices))

def test():
    assert answer('100 200 300 400 500 600') == 400
    assert answer('14324 8678 423 980') == 980
    assert answer('987 213 10000 2 1231') == 989
    print('all test cases passed...')

if __name__=="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test()
    else:
        solve()
