class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        list_tmp = []
        list_tmp.append('1')
        i = 1
        while i < n:
            str_tmp1 = list_tmp[i - 1]
            str_tmp2 = ''
            j = 0
            j_count = 1
            while j < len(str_tmp1) - 1:
                if str_tmp1[j + 1] == str_tmp1[j]:
                    j_count += 1
                else:
                    str_tmp2 += str(j_count)
                    str_tmp2 += str_tmp1[j]
                    j_count = 1
                j += 1
            str_tmp2 += str(j_count)
            str_tmp2 += str_tmp1[-1]
            list_tmp.append(str_tmp2)
            i += 1

        for tmp in list_tmp:
            print(tmp)

sl = Solution()
sl.countAndSay(5)
