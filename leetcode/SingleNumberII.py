class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def singleNumber1(self, nums):
        retVal = 0
        nMask = 1 << 31
        while nMask > 0:
            bitSum = 0
            for i in range(len(nums)):
                if nums[i] & nMask == nMask:
                    bitSum += 1
            nBits = bitSum % 3
            if nBits == 1:
                retVal += nMask
            nMask >>= 1
        if retVal > (1 << 31):
            retVal = retVal - (1 << 32)
        return retVal
    def singleNumber(self, nums):
        ones = 0
        twos = 0
        threes = 0
        for i in range(len(nums)):
            twos |= ones & nums[i]
            ones ^= nums[i]
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
        return ones
sl = Solution()
print(sl.singleNumber([-2,-2,1,1,-3,1,-3,-3,-7,-2]))