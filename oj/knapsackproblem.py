'''
Created on 2015/6/20

@author: FEIHUA
'''
class Solution:
    def knapsack(self, weightList, valueList, weightSum):        
        m = len(valueList)
        sumList = []
        for i in range(m):
            sumList.append([])
            for j in range(weightSum):
                if j > weightList[i]:
                    if i >= 1:
                        sumList[i].append(max(sumList[i - 1][j], sumList[i - 1][j - weightList[i]] + valueList[i]))
                    else:
                        sumList[i].append(valueList[i])
                else:
                    if i >= 1:
                        sumList[i].append(sumList[i - 1][j])
                    else:
                        sumList[i].append(0)
        print(sumList)        
        return

sl = Solution()
sl.knapsack([2,2,6,5,4], [6,3,5,4,6], 10)