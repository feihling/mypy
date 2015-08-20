'''
Created on 2015-5-29

@author: lingfeihua
'''
class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def insertToList(self, lists, n):
        k = 0
        l = len(lists)
        while k < l:
            j = (k + l) / 2
            print 'j(%s) k(%s) l(%s) total(%s)' % (j, k, l, len(lists))
            if n < lists[j]:
                k = j + 1
            elif n > lists[j]:
                l = j - 1
            else:
                k = j
                break
        print 'j(%s) k(%s) l(%s) total(%s)' % (j, k, l, len(lists))
        if k == len(lists):
            lists.append(n)
        else:
            lists.insert(k, n)
        return lists

sl = Solution()
print sl.insertToList([9, 7, 5, 1],  4)
print sl.insertToList([9, 7, 5, 4],  5)
print sl.insertToList([9, 7, 5, 4],  10)
print sl.insertToList([1],  0)
print sl.insertToList([0],  1)