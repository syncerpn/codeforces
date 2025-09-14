t = int(input())
def split(s):
    ans = []
    d, k = s[0], 1
    for i in range(1, len(s)):
        if s[i] == d:
            k += 1
        else:
            ans.append((d, k))
            d = s[i]
            k = 1
    ans.append((d, k))
    return ans
        
for _ in range(t):
    p = input()
    s = input()
    
    pp = split(p)
    ss = split(s)
    if len(pp) != len(ss):
        print("NO")
    else:
        for pi, si in zip(pp, ss):
            pid, pik = pi
            sid, sik = si
            if pid != sid:
                print("NO")
                break
            elif sik > 2 * pik or sik < pik:
                print("NO")
                break
        else:
            print("YES")