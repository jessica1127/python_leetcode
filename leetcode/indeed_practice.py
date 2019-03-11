
'''
Time limit : 2sec / Memory limit : 256MB

Score : 100 points

Problem Statement
You are given N records.
The content of the i-th record is represented by a string Si.
These records are managed in pages, as follows:

The first page: contains the first, ..., K-th records.
The second page: contains the (K+1)-th, ..., 2K-th records.
The third page: contains the (2K+1)-th, ..., 3K-th records.
:
The ceil(N⁄K)-th page: contains the ((ceil(N⁄K)−1)K+1)-th, ..., N-th records.
Here, ceil(X) represents the smallest integer not less than X.
Print the contents of the records contained in the M-th page, in the order given.

Constraints
1≤N≤100
1≤K≤N
1≤M≤ceil(N⁄K)
1≤|Si|≤100 (1≤i≤N), where |S| is the length of S.
Si is a string consisting of lowercase English letters.
Input
Input is given from Standard Input in the following format:

N K M
S1
S2
:
SN
Output
Print the contents of the records contained in the M-th page, in the order given.
Use L lines, where L is the number of records that should be printed.
The i-th line (1≤i≤L) should contain the content of the i-th record contained in the M-th page.

Sample Input 1
Copy
5 2 2
aaa
bbb
ccc
ddd
eee
Sample Output 1
Copy
ccc
ddd
The first page contains the first and second records, which are aaa and bbb.
The second page contains the third and fourth records, which are ccc and ddd.
The third page contains the fifth record, which is eee.
Since the second page is requested, we should print ccc in the first line and ddd in the second line.

Sample Input 2
Copy
7 4 2
this
is
not
displayed
this
is
displayed
Sample Output 2
Copy
this
is
displayed
Sample Input 3
Copy
10 4 1
mzbmweyydiadtlcouegmdbyfwurpwbpuvhifnuapwynd
htqvkgkbhtytszotwflegsjzzszfwtz
pnscguemwrczqxycivdqnkypnxnnpmuduhznoaquudhavrncwfwujpcmiggjmcmkkbnjfeodxkgjgwxtrxin
iqquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfis
ulgbglwm
gzrnyxryetwzhlnfewczmnoozl
atugmdjwgzcfabbkoxyjxkatjmpprswkdkobdagwdwxsufeesrvncbszcep
gpbzuzo
otorzfskcwbqorvwdrmklfdczatfarqdkelalxzxillkfdvpfpxabqlng
screntzamztvvcvrtcmbqlizijdwtuyfrxolsysxlfebpolcmqsppmrfkyunyd
Sample Output 3
Copy
mzbmweyydiadtlcouegmdbyfwurpwbpuvhifnuapwynd
htqvkgkbhtytszotwflegsjzzszfwtz
pnscguemwrczqxycivdqnkypnxnnpmuduhznoaquudhavrncwfwujpcmiggjmcmkkbnjfeodxkgjgwxtrxin
iqquhuwqhdswxxrxuzzfhkplwunfagppcoildagktgdarveusjuqfis
Submit

Personal Information Tutorial Rules Glossary FAQ
Powered by AtCoder.
'''
import sys
n = 0
lines = []
try:
    for line in sys.stdin:
        n += 1
        if n == 1:
            N, K, M = map(int, line.split())
        else:
            lines.append(line.rstrip("\n"))
    if K != 0 and M >=1:
        page_index = N//K *(M-1)
    for i in range(page_index, page_index+K):
        print lines[i]
except:
    pass

# N, K, M = map(int, raw_input().split())
# print "N = ", N, "K= ",K,"M=",M

# try:
#     for i in range(N):
#         Si = sys.stdin.readline()
#         print Si
# except:
#     pass