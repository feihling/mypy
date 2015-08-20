class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        i = 0
        dict_res = {}
        while i < len(strs):
            dict_word = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in dict_word:
                    dict_word[strs[i][j]] = 1
                else:
                    dict_word[strs[i][j]] += 1
            str_word = ''
            for each_key in sorted(dict_word.keys()):
                str_word += each_key
                str_word += str(dict_word[each_key])
            
            if str_word not in dict_res:
                dict_res[str_word] = []
                dict_res[str_word].append(strs[i])
            else:
                dict_res[str_word].append(strs[i])
            i += 1

        ret_list = []
        for each_key in dict_res:
            print('%s:%s' % (each_key, dict_res[each_key]))
            if len(dict_res[each_key]) > 1:
                ret_list += dict_res[each_key]
        return ret_list

sl = Solution()
print(sl.anagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"] ))
