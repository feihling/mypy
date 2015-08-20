class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        irDict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        n = 1000
        tmp = num
        ret = ''
        while n > 0:
            bitNum = tmp // n
            tmp = tmp % n
            if bitNum == 0:
                pass
            elif bitNum < 4:
                ret += irDict[n] * bitNum
            elif bitNum == 4:
                ret += irDict[n] + irDict[5*n]
            elif bitNum == 9:
                ret += irDict[n] + irDict[10*n]
            else:
                ret += irDict[5*n] + irDict[n] * (bitNum - 5)
            n = n // 10
        print(ret)
        return ret
sl = Solution()
sl.intToRoman(1)