'''
Created on 2015-5-15

@author: lingfeihua
'''
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        ret_str = ''
        bit_u = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            if i < 0:
                bit_b = ord(b[j]) - ord('0')
                ret_str = str(bit_b ^ bit_u) + ret_str
                bit_u = bit_b & bit_u
            elif j < 0:
                bit_a = ord(a[i]) - ord('0')
                ret_str = str(bit_a ^ bit_u) + ret_str
                bit_u = bit_a & bit_u
            else:
                bit_a = ord(a[i]) - ord('0')
                bit_b = ord(b[j]) - ord('0')
                ret_str = str((bit_a ^ bit_b) ^ bit_u) + ret_str
                bit_u = (bit_a & bit_b) | (bit_a ^ bit_b) & bit_u
            i -= 1
            j -= 1
        if bit_u == 1:
            return '1' + ret_str
        else:
            return ret_str
    
sl = Solution()
print sl.addBinary('11', '11')