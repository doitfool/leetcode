# coding: utf-8
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            result = ""
        else:
            temp = []
            min_len = min([len(s) for s in strs])
            for i in xrange(min_len):
                flag = True
                for j in xrange(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        flag = False
                        break
                if flag:
                    temp.append(strs[0][i])
                else:
                    break
            result = ''.join(temp)
        return result

if __name__ == '__main__':
    s = Solution()
    print s.longestCommonPrefix(['abc', 'ab', 'abcd'])



