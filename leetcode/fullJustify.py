class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        i = 0
        ret_str = []
        while i < len(words):
            cur_len = len(words[i])
            j = i
            while cur_len <= maxWidth:
                j += 1
                if j >= len(words):
                    break
                cur_len += len(words[j])
                cur_len += 1                

            if j >= len(words):
                #last line
                tmp_str = ''
                m = i
                while (m < j - 1):
                    tmp_str += words[m] + ' '
                    m += 1
                tmp_str += words[j - 1] + (maxWidth - cur_len - 1) * ' '
                ret_str.append(tmp_str)
                i = j            
            elif cur_len - 1 == maxWidth:
                print(words[i:j+1])
                ret_str.append(' '.join(words[i:j+1]))
                i = j + 1
            else:
                if j - i == 1:
                    ret_str.append(words[i] + (maxWidth - len(words[i])) * ' ')
                else:                        
                    cur_len = cur_len - len(words[j]) -2
                    extra_space = maxWidth - cur_len
                    k = extra_space // (j - i - 1)
                    l = extra_space % (j - i - 1)
                    m = i
                    tmp_str = ''
                    while (m < j - 1):
                        if l > 0:
                            tmp_str += words[m] + (k + 2) * ' '
                            l -= 1
                        else:
                            tmp_str += words[m] + (k + 1) * ' '
                        m += 1
                    tmp_str += words[j - 1]
                    ret_str.append(tmp_str)
                i = j

        return ret_str

sl = Solution()
print(sl.fullJustify(["Here","is","an","example","of","text","justification."], 14))

        
