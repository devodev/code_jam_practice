"""
Source: https://github.com/devodev/code_jam_practice/tree/master/contests/2008

Problem: A
Link: https://code.google.com/codejam/contest/dashboard?c=32013#s=p0
"""

# Problem

# The urban legend goes that if you go to the Google homepage and search for "Google", the universe will implode.
# We have a secret to share... It is true! Please don't try it, or tell anyone.
# All right, maybe not. We are just kidding.

# The same is not true for a universe far far away.
# In that universe, if you search on any search engine for that search engine's name, the universe does implode!

# To combat this, people came up with an interesting solution.
# All queries are pooled together.
# They are passed to a central system that decides which query goes to which search engine.
# The central system sends a series of queries to one search engine, and can switch to another at any time.
# Queries must be processed in the order they're received.
# The central system must never send a query to a search engine whose name matches the query.
# In order to reduce costs, the number of switches should be minimized.

# Your task is to tell us how many times the central system will have
#   to switch between search engines, assuming that we program it optimally. 


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