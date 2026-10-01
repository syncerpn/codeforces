import math

def sqd(a):
    ans = 0
    while a > 0:
        d = a % 10
        ans += d * d
        a //= 10
    return ans

def cycle(a):
    repeat = None
    states = []
    sset = {}
    while a not in sset:
        sset[a] = len(states)
        states.append(a)
        a = sqd(a)
    repeat = sset[a]
    return (states, repeat)

def tune(sra, srb):
    sa, ra = sra
    sb, rb = srb
    
    la = len(sa)
    pa = la - ra
    
    lb = len(sb)
    pb = lb - rb
    
    m = math.lcm(pa, pb)
    r = max(la, lb)
    for i in range(r, r + m):
        ia = ra + (i - la) % pa
        ib = rb + (i - lb) % pb
        if sa[ia] != sb[ib]:
            return False
    return True
    

t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int, input().strip().split(" ")))
    B = [cycle(a) for a in A]
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if tune(B[i], B[j]):
                ans += 1
    print(ans)