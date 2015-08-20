#coding=utf-8
'''
Created on 2015年5月30日

@author: FEIHUA
'''
def binarayInsert(lists, n):
    nlow = 0
    nhigh = len(lists) - 1
    while nlow <= nhigh:
        print('nlow(%s), nhigh(%s)' % (nlow, nhigh))
        mid = (nlow + nhigh) // 2
        print('mid(%s)' % mid)
        if n < lists[mid]:
            nlow = mid + 1
        else:
            nhigh = mid - 1
    print('nlow(%s), nhigh(%s)' % (nlow, nhigh))
    if nlow > len(lists) - 1:
        lists.append(n)
    else:
        lists.insert(nlow, n)
    return lists
print(binarayInsert([10, 8, 7], 1))
print(binarayInsert([10, 8, 7, 1], 1))
print(binarayInsert([1], 0))