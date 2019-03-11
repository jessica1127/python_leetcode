'''
D - 駅巡り / Station Tour
Time limit : 2sec / Memory limit : 256MB

Score : 100 points

Problem Statement
There are N stations in a certain region, numbered 1 through N.
It takes di,j minutes to travel from Station i to Station j (1 \leq i, j \leq N)$.
Note that di,j=dj,i may not hold.

You are now at Station 1. From here, you have to visit all the stations exactly once.
We assume that you have already visited Station 1.
However, due to your schedule, there are M restrictions that must be satisfied.
The format of each restriction is as follows:

Station si must be visited before Station ti. (1≤i≤M)
Find the minimum time required to visit all the stations.
Note that the last station to visit can be any of the stations.

Constraints
1≤N≤14
0≤di,j≤108 (1≤i,j≤N)
di,i=0 (1≤i≤N)
0≤M≤N(N−1)⁄2
1≤si,ti≤N (1≤i≤M)
si≠ti (1≤i≤M)
There exists a path visiting all the stations under the given restrictions.
Input
Input is given from Standard Input in the following format:

N
d1,1 … d1,N
:
dN,1 … dN,N
M
s1 t1
:
sM tM
Output
Print the minimum time required to visit all the stations.

Sample Input 1
Copy
4
0 2 3 4
1 0 3 4
1 2 0 4
1 2 3 0
3
1 2
2 3
3 4
Sample Output 1
Copy
9
Due to the restrictions, we can only travel as follows: Station 1 → Station 2 → Station 3 → Station 4.
Thus, the answer is 2+3+4=9 and we should print 9.

Sample Input 2
Copy
3
0 1 20
1 0 20
10 20 0
0
Sample Output 2
Copy
21
Sample Input 3
Copy
1
0
0
Sample Output 3
Copy
0
Sample Input 4
Copy
14
0 28448202 94752369 6965437 42744902 7560126 75090662 8843627 69061140 64249326 57690728 42986477 48404113 88716403
73013281 0 37847212 34428188 25009906 3614271 82144791 23149022 94211619 56083883 547750 35036479 37794350 85146222
6400137 79121726 0 32137663 86550075 54343753 78531432 1169605 56872598 61793842 30013621 61824448 76242267 78181546
44000464 19945953 92672933 0 8488951 29783495 42361540 61448706 5092013 39670396 92639393 26910058 56878215 83406982
42411559 55713387 40842605 80915875 0 90870302 16746891 41698332 92400406 79586785 76734482 54938846 14817854 44262797
25618079 82961670 3220380 37882710 77238264 0 30285694 94010597 3313434 25248938 6148456 57383107 80041226 52974537
45702192 36993407 35034648 13099849 97787850 79254364 0 44172314 73023554 53984059 83657376 26813141 8449228 85695371
89466424 82640627 2816597 1216033 21988152 90828105 83428522 0 216303 46837120 30499660 38938821 68789759 30497390
14240720 49216529 36512207 64082795 92391305 70382708 28258331 4979511 0 884770 66017741 51457552 4005017 50751247
15122265 49804986 83078215 87707425 56873145 88791801 34219986 77073154 82798626 0 7386614 49058658 3482690 55300190
96344094 77929649 15796809 35347942 46688706 15359332 64653788 87407203 42689175 98416950 0 83290181 47967318 90377000
27375431 9920337 23971212 20418378 68812572 23746130 78728346 72070698 1939257 87280009 11983259 0 37799770 16442015
85303335 55565703 5694284 91866847 29725710 98189375 17777160 81031919 59126600 83771749 67762666 68788386 0 75480673
54861272 25070911 78287445 76137950 81268769 83585267 49252003 71439588 98965870 54719898 78225858 25335948 85354514 0
7
12 7
1 7
8 5
11 3
14 6
4 13
8 9
Sample Output 4
Copy
146741852
Submit

Personal Information Tutorial Rules Glossary FAQ
Powered by AtCoder.
'''