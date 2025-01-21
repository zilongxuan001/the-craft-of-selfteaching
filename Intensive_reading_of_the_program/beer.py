

"""
A Python version of the classic "bottles of beer on the wall" programming
example.

By Guido van Rossum, demystified after a version by Fredrik Lundh.
"""

import sys

n = 100
sys.argv = ['demo.py', '1', '2', '3'] # 建立列表
if sys.argv[1:]:
    n = int(sys.argv[1])


def bottle(n):
    if n == 0: return "no more bottles of beer"  #  没有回行，直接返回值。
    if n == 1: return "one bottle of beer"
    return str(n) + " bottles of beer"

for i in range(n, 0, -1): # range(n,0,-1) 从n开始，到1，步长为-1。
    print(bottle(i), "on the wall,")
    print(bottle(i) + ".")
    print("Take one down, pass it around,")
    print(bottle(i-1), "on the wall.")


