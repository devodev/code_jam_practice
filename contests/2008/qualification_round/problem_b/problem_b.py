"""
Source: https://github.com/devodev/code_jam_practice/tree/master/contests/2008

Problem: B
Link: https://code.google.com/codejam/contest/dashboard?c=32013#s=p1
"""

# Input

# The first line of input gives the number of cases, N. N test cases follow.

# Each case contains a number of lines.
# The first line is the turnaround time, T, in minutes.
# The next line has two numbers on it, NA and NB.
# NA is the number of trips from A to B, and NB is the number of trips from B to A.
# Then there are NA lines giving the details of the trips from A to B.

# Each line contains two fields, giving the HH:MM departure and arrival time for that trip.
# The departure time for each trip will be earlier than the arrival time.
# All arrivals and departures occur on the same day.
# The trips may appear in any order - they are not necessarily sorted by time.
# The hour and minute values are both two digits, zero-padded, and are on a 24-hour clock (00:00 through 23:59).

# After these NA lines, there are NB lines giving the departure and arrival times for the trips from B to A.

# Output
# For each test case, output one line containing "Case #x: " followed by
#   the number of trains that must start at A and the number of trains that must start at B.

# Limits
# 1 ≤ N ≤ 100

# Small dataset
# 0 ≤ NA, NB ≤ 20
# 0 ≤ T ≤ 5

# Large dataset
# 0 ≤ NA, NB ≤ 100
# 0 ≤ T ≤ 60


N = int(input())
count = 0
for i in range(N):
    print('Case #{}: {}'.format(i + 1, count))