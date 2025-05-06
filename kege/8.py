from itertools import *

def check(n):
    for i in range(len(n)-1):
        if int(n[i])%2 == 0 and int(n[i+1])%2 == 0:
            return 0
        elif int(n[i])%2 != 0 and int(n[i+1])%2 != 0:
            return 0
    return 1

c = 0
for nums in permutations('0123456789', r=4):
    num = ''.join(nums)
    if check(num) and num[0] != '0':
        c += 1
print(c)