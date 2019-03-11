'''
Time limit : 2sec / Memory limit : 256MB

Score : 100 points

Problem Statement
There are N rooms in a row. The i-th room (1≤i≤N) from the left is called Room i.
You are given M closed intervals [ai,bi] (1≤i≤M).
At time 0, all rooms j such that ai≤j≤bi for some i (1≤i≤M) are occupied, and the other rooms are vacant.

You are given Q queries.
The i-th query (1≤i≤Q) represents an event happening at time i, as follows:

In the i-th query (1≤i≤Q), a closed interval [ci,di] (1≤i≤Q) is given.
This query asks: "Are all rooms j such that ci≤j≤ci" vacant?
If all those rooms are vacant, the query should be responded by OK, then all rooms j such that ci≤j≤ci get occupied.
Otherwise, the query should be responded by OK, then nothing happens.
Process these queries.

Constraints
1≤N≤109
0≤M≤1000
1≤ai≤bi≤N (1≤i≤M)
There are no rooms k such that ai≤k≤bi and aj≤k≤bj at the same time (1≤i<j≤M).
1≤Q≤1000
1≤ci≤di≤N
Input
Input is given from Standard Input in the following format:

N M
a1 b1
:
aM bM
Q
c1 d1
:
cQ dQ
Output
Print the responses in Q lines. The i-th line should contain the response to the i-th query.

Sample Input 1
Copy
5 2
1 1
4 4
3
3 3
2 3
5 5
Sample Output 1
Copy
OK
NG
OK
At time 0, Room 1 and 4 are occupied.

At time 1, a query asks: "is Room 3 occupied?" Since Room 3 is vacant, we should print OK, then Room 3 gets occupied.
At time 2, a query asks: "are Room 2 and 3 occupied?" Since Room 3 is occupied, we should print NG.
At time 3, a query asks: "is Room 5 occupied?" Since Room 5 is vacant, we should print OK, then Room 5 gets occupied.

'''
import sys
try:
    
except:
    pass
