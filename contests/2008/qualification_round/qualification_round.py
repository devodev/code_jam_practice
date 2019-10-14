"""
Source: https://github.com/devodev/code_jam_practice/blob/master/contests/2008/qualification_round.py
Author: https://github.com/devodev
"""

# Input

# The first line of the input file contains the number of cases, N. N test cases follow.

# Each case starts with the number S -- the number of search engines.
#
# The next S lines each contain the name of a search engine.
# Each search engine name is no more than one hundred characters long and
#   contains only uppercase letters, lowercase letters, spaces, and numbers.
# There will not be two search engines with the same name.

# The following line contains a number Q -- the number of incoming queries.
#
# The next Q lines will each contain a query.
# Each query will be the name of a search engine in the case.

# Output
# For each input case, you should output:
# Case #X: Y
# where X is the number of the test case and Y is the number of search engine switches.
# Do not count the initial choice of a search engine as a switch.

# Limits
# 0 < N ≤ 20

# Small dataset
# 2 ≤ S ≤ 10
# 0 ≤ Q ≤ 100

# Large dataset
# 2 ≤ S ≤ 100
# 0 ≤ Q ≤ 1000 
#

N = int(input())
for i in range(N):
    S = int(input())
    for y in range(S):
        input()

    Q = int(input())
    q_set = set()
    count  = 0
    for z in range(Q):
        input_str = input()
        if input_str not in q_set:
            if len(q_set) == S-1:
                q_set.clear()
                count += 1
            q_set.add(input_str)

    print('Case #{}: {}'.format(i + 1, count))