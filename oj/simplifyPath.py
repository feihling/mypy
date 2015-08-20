class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        new_str = ''
        new_str_len = 0
        i = 0
        while i < len(path):
            j = i + 1
            while j < len(path) and path[j] != '/':
                j += 1
            print('i{}:j{}: {}', i, j, path[i:j])
            if path[i:j] == '/..':
                if new_str_len > 0:
                    k = new_str_len - 1
                    while (new_str[k] != '/'):
                        k -= 1
                    new_str = new_str[0:k]
                    new_str_len = k
            elif j - i != 1 and path[i:j] != '/.':
                new_str += path[i:j]
                new_str_len += j - i

            i = j

        if new_str == '':
            return '/'
        else:
            return new_str

        
sl = Solution()
print(sl.simplifyPath("////../../././"))
print(sl.simplifyPath("///../../F/./rVH/jmkyl/wpxS/sRC/cL/NR///tO/./"))
