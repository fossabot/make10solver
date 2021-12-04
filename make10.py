#!/usr/bin/env python3

import sys
import argparse
from fractions import Fraction

## pattern
## ((a,b),c),d
## (a,b),(c,d)
## (a,(b,c)),d
## a,((b,c),d)
## a,(b,(c,d))

def fadd(f1, f2):
    return f1 + f2
def fsub(f1, f2):
    return f1 - f2
def fmul(f1, f2):
    return f1 * f2
def fdiv(f1, f2):
    if f2 == 0:
        return Fraction(9999999,101)
    return f1 / f2

def print_num4(ptn, fnums, ops):
    patterns = [
        "(({} {} {}) {} {}) {} {}",
        "({} {} {}) {} ({} {} {})",
        "({} {} ({} {} {})) {} {}",
        "{} {} (({} {} {}) {} {})",
        "{} {} ({} {} ({} {} {}))",
        ""
        ]
    sops = []
    for op in ops:
        if op == fadd:
            sops.append("+")
        elif op == fsub:
            sops.append("-")
        elif op == fmul:
            sops.append("*")
        else:
            sops.append("/")
    print(patterns[ptn].format(fnums[0], sops[0], fnums[1], sops[1], fnums[2], sops[2], fnums[3]))

def solve_each(ptn, fnums, op1, op2, op3, displayf):
    if ptn == 0:
        fret = op3(op2(op1(fnums[0], fnums[1]), fnums[2]), fnums[3])
    elif ptn == 1:
        fret = op2(op1(fnums[0], fnums[1]), op3(fnums[2], fnums[3]))
    elif ptn == 2:
        fret = op3(op1(fnums[0], op2(fnums[1], fnums[2])), fnums[3])
    elif ptn == 3:
        fret = op1(fnums[0], op3(op2(fnums[1], fnums[2]), fnums[3]))
    else:
        fret = op1(fnums[0], op2(fnums[1], op3(fnums[2], fnums[3])))
    if fret == 10:
        if displayf:
            print_num4(ptn, fnums, [op1, op2, op3])
        return 1
    return 0

def solvef(fnums, displayf):
    ans = 0
    for op1 in [fadd, fsub, fmul, fdiv]:
        for op2 in [fadd, fsub, fmul, fdiv]:
            for op3 in [fadd, fsub, fmul, fdiv]:
                for ptn in [0,1,2,3,4]:
                    ans += solve_each(ptn,fnums,op1,op2,op3,displayf)
    return ans

def solve(nums, displayf=True):
    for n in nums:
        if n < 0 or n > 9:
            print("out of range:{}".format(n))
            return
    ans = 0
    donenum = {}
    for i in [0,1,2,3]:
        for j in [0,1,2,3]:
            for k in [0,1,2,3]:
                if i != j and i != k and j != k:
                    l = 6 - i - j - k
                    n = nums[i]*1000+nums[j]*100+nums[k]*10+nums[l]
                    if not n in donenum:
                        donenum[n] = True
                        fnums = [Fraction(nums[i]), Fraction(nums[j]),
                                 Fraction(nums[k]), Fraction(nums[l])]
                        ans += solvef(fnums, displayf)
    return ans

def divide_nums(n):
    return [int(n/1000)%10, int(n/100)%10, int(n/10)%10, n%10]

def search_all(upper):
    n = 0
    i = 0
    while n < 10000:
        nums = divide_nums(n)
        if nums[0] <= nums[1] and nums[1] <= nums[2] and nums[2] <= nums[3]:
            ans = solve(nums, False)
            if ans > 0 and ans <= upper:
                print(nums)
            i += 1
            if i == 10:
                i = 0
                sys.stdout.write('.')
                sys.stdout.flush()
        n += 1
    sys.stdout.write('\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="make10 solver")
    parser.add_argument('num', type=int, help="number to be checked")
    args = parser.parse_args()
    if args.num < 0:
        search_all(-args.num)
    else:
        ans = solve(divide_nums(args.num))
        print("Total {} answers".format(ans))
