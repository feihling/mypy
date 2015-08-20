'''
Created on 2015-7-10

@author: lingfeihua
'''
class Solution:
    # @param {integer[][]} buildings
    # @return {integer[][]}
    def getSkyline(self, buildings):
        n = len(buildings)
        if n == 0:
            return []
        if n == 1:
            return [[buildings[0], buildings[2]], [buildings[1], 0]]
        return self.mergeSkyline(self.getSkyline(buildings[: n // 2]), self.getSkyline(buildings[n // 2 + 1 :]))
    
    def mergeSkyline(self, lSkyline, rSkyline):
        ret = [lSkyline[0]]
        l = len(lSkyline)
        r = len(rSkyline)
        i = 1
        j = 0
        lFlag = True
        while i < l and j < r:
            if lSkyline[i][0] < rSkyline[j][0]:
                if not lFlag:
                    if lSkyline[i][1] > ret[-1][1]:
                        ret.append(lSkyline[i])
                        lFlag = True
                    elif lSkyline[i][1] == ret[-1][1]:
                        ret[-1][0] = lSkyline[i][0]
                        lFlag = True
                else:
                    ret.append(lSkyline[i])
                i += 1                    
            elif lSkyline[i][0] > rSkyline[j][0]:
                if lFlag:
                    if rSkyline[j][1] > ret[-1][1]:
                        ret.append(rSkyline[j])
                        lFlag = False
                    elif rSkyline[j][1] == ret[-1][1]:
                        ret[-1][0] = rSkyline[j][0]
                        lFlag = False
                else:
                    ret.append(rSkyline[j])
                j += 1
            else:
                if lSkyline[i][1] > rSkyline[j][1]:
                    curNode = lSkyline[i]
                    lFlag = True
                else:
                    curNode = rSkyline[j]
                    lFlag = False
                i += 1
                j += 1

        
        return ret