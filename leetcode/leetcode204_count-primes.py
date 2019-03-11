'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

note: include 0~n
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes = [True] * n   
        primes[0] = primes[1] = False  #0 and 1 are not prime numbers
        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                primes[i*i : n : i ] = [False] * len(primes[i * i: n: i])
        return sum(primes)

        
s = Solution()
n = 100
ret = s.countPrimes(100)
print ret