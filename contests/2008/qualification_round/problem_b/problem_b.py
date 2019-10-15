"""
Source: https://github.com/devodev/code_jam_practice/tree/master/contests/2008

Problem: B
Link: https://code.google.com/codejam/contest/dashboard?c=32013#s=p1
"""

# Problem

# A train line has two stations on it, A and B.
# Trains can take trips from A to B or from B to A multiple times during a day.
# When a train arrives at B from A (or arrives at A from B), it needs a certain amount
#   of time before it is ready to take the return journey - this is the turnaround time.
# For example, if a train arrives at 12:00 and the turnaround time is 0 minutes, it can leave immediately, at 12:00.

# A train timetable specifies departure and arrival time of all trips between A and B.
# The train company needs to know how many trains have to start the day at A and B in order
#   to make the timetable work: whenever a train is supposed to leave A or B, there must actually be one there ready to go.
# There are passing sections on the track, so trains don't necessarily arrive in the same order that they leave.
# Trains may not travel on trips that do not appear on the schedule. 


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

import datetime

N = int(input())
for i in range(N):
    T = int(input())
    NA, NB = [int(s) for s in input().split(' ')]

    start_a = NA
    start_b = NB
    for y in range(NA):
        departure, arrival = [datetime.time(*s.split(':')) for s in input().split(' ')]
        
    for z in range(NB):
        departure, arrival = [datetime.time(*s.split(':')) for s in input().split(' ')]


    print('Case #{}: {} {}'.format(i + 1, start_a, start_b))
    