def longestConsecutive(nums):
    dict_tmp = {}
    for each_num in nums:
        dict_tmp[each_num] = 1
    res = 0
    for each_num in nums:
        if dict_tmp[each_num] == 1:
            dict_tmp[each_num] = 0
            sum = 1
            tmp = each_num - 1
            while (tmp in dict_tmp):
                dict_tmp[tmp] = 0
                sum += 1
                tmp = tmp - 1
                
            tmp = each_num + 1
            while (tmp in dict_tmp):
                dict_tmp[tmp] = 0
                sum += 1
                tmp = tmp + 1

            if sum > res:
                res = sum
    return res

print(longestConsecutive([1,2,3,4,5]))
