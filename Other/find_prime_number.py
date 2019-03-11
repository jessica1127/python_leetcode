'''
Find a  prime number, the prime number is 0 ~ N
'''
class Solution():

    def find_prime(self, n):
        res = [True] * n
        res[0] = res[1] = False  # 0 and 1 are not prime numbers

        for i in range(2, int(n**.5)+1):
            if res[i]:   #if res[i] has not been visited:
                res[i*i : n : i] = [False] * len(res[i*i : n : i])
        return sum(res)

s = Solution()
n = 100
print s.find_prime(n)