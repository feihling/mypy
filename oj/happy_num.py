class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        tmp_list = []
        tmp = 0
        while tmp != 1:
            tmp = 0
            while n != 0:
                tmp += (n % 10) * (n % 10)
                n = n // 10
            if tmp not in tmp_list:
                print(tmp)
                tmp_list.append(tmp)
            else:
                print(tmp)
                return False
            n = tmp
        return True

sl = Solution()
print('result: {}', sl.isHappy(2147483647))
