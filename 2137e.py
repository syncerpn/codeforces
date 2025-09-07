t = int(input())
for _ in range(t):
    n, k = list(map(int, input().strip().split(" ")))
    A = list(map(int, input().strip().split(" ")))
    S = set(list(range(n+1)))
    states = {}
    steps = []
    dp = [0] * (n+1)
    for a in A:
        dp[a] += 1
        S.discard(a)
    m = min(S)
    tdp = tuple(dp)
    states[tdp] = 0
    steps.append(tdp)
    while k > 0:
        k -= 1
        m_next = n+1
        dp_next = [0] * (n+1)
        for i in range(n+1):
            if i == m:
                continue
            if i > m or dp[i] > 1:
                dp_next[m] += dp[i]
                dp_next[i] = 0
                m_next = min(m_next, i)
            else:
                dp_next[i] = dp[i]
        dp = dp_next
        m = m_next
        tdp = tuple(dp)
        if tdp in states:
            break
        steps.append(tdp)
        states[tdp] = len(steps) - 1
    
    last_step = states[tdp]
    end_step = last_step + k % (len(steps) - last_step)
    tdp = steps[end_step]
    print(sum(i*tdp[i] for i in range(n+1)))