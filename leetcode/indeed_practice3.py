#coding: utf-8
'''
C - 部分列の最大値 / Maximums in Intervals
Time limit : 2sec / Memory limit : 256MB

Score : 100 points

Problem Statement
You are given an array of length N consisting of integers, a={a1,…,aN}, and an integer L.

Consider the following subproblem:

You are given an integer S.
Find the largest value in the interval [S,S+L−1] in the sequence a, that is, find max(aS,…,aS+L−1).
Solve this subproblem for every S=1,…,N−L+1.

Constraints
1≤N≤105
1≤L≤N
−109≤ai≤109
Input
Input is given from Standard Input in the following format:

N L
a1 … aN
Output
Print the answers in N−L+1 lines.
The i-th line should contain the answer to the subproblem where S=i.

Sample Input 1
Copy
5 3
3 4 2 1 5
Sample Output 1
Copy
4
4
5
The subproblem where S=1 asks the largest value among a={a1,a2,a3}={3,4,2}, so the first line in the output should contain 4.
The subproblem where S=2 asks the largest value among a={a2,a3,a4}={4,2,1}, so the second line in the output should contain 4.
The subproblem where S=3 asks the largest value among a={a3,a4,a5}={2,1,5}, so the third line in the output should contain 5.
Sample Input 2
Copy
4 1
-1000000000 1000000000 -1000000000 1000000000
Sample Output 2
Copy
-1000000000
1000000000
-1000000000
1000000000
Sample Input 3
Copy
10 5
-253230108 363756450 712662868 735867677 193944314 586260100 -192321079 95834122 802780784 418379342
Sample Output 3
Copy
735867677
735867677
735867677
735867677
802780784
802780784
'''
import sys

n = 0
a = []
try:
    for line in sys.stdin:
        n += 1
        if n == 1:
            N, L = map(int, line.split())
        elif n == 2:
            a = line.rstrip("\n").split(" ")
    print "N = ", N, "L = ", L , " a = ", a
    for i in xrange(L):
        print max(a[i:L+i])
except:
    pass
    