import re

if __name__ == '__main__':
    L, D, N = map(int, input().split())
    words = [input() for _ in range(D)]
    test_cases = [input() for _ in range(N)]
    m = re.compile(r'\(([a-z]+)\)|([a-z])')
    for i in range(N):
        matcher = [x[0] if x[0] else x[1] for x in m.findall(test_cases[i]) if x]
        matched = 0
        for w in words:
            for idx, c in enumerate(w):
                if c not in matcher[idx]:
                    break
                if idx == L-1:
                    matched += 1
        print("Case #{}: {}".format(i+1, matched))
