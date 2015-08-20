class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        ver_list1 = version1.split('.')
        ver_list2 = version2.split('.')
        ver_len = 0
        flag = 0
        if len(ver_list1) < len(ver_list2):
            ver_len = len(ver_list1)
            flag = -1
        elif len(ver_list1) > len(ver_list2):
            ver_len = len(ver_list2)
            flag = 1
        else:
            ver_len = len(ver_list1)

        print('flag {}', flag)
        print('ver_len {}', ver_len)
        for i in range(ver_len):
            if int(ver_list1[i]) > int(ver_list2[i]):
                print(ver_list1[i])
                print(ver_list2[i])
                return 1
            elif int(ver_list1[i]) < int(ver_list2[i]):
                return -1
        
        if flag == 1:
            for i in range(ver_len, len(ver_list1)):
                if int(ver_list1[i]) > 0:
                    return flag
        elif flag == -1:
            for i in range(ver_len, len(ver_list2)):
                if int(ver_list2[i]) > 0:
                    return flag
        
        return flag

sl = Solution()
print(sl.compareVersion('1.0', '1'))
