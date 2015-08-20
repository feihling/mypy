'''
Created on 2015-7-29

@author: lingfeihua
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        is_prime = [True] * n
        if n <= 1:
            return 0
        i = 2
        while i * i < n:
            if is_prime[i]:
                j = i * i
                while j < n:
                    is_prime[j] = False
                    j += i
            i += 1
        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1
        return count
    
sl = Solution()
print(sl.countPrimes(1))
print(sl.countPrimes(2))
print(sl.countPrimes(3))
print(sl.countPrimes(4))
print(sl.countPrimes(5))
print(sl.countPrimes(10))
print(sl.countPrimes(499979))
print(sl.countPrimes(1500000))