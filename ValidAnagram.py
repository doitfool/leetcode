"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution(object):
    def str2dic(self, s):
        d = {}
        for i in xrange(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        return d
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = self.str2dic(s)
        t_dic = self.str2dic(t)
        if len(s_dic) != len(t_dic):
            flag = False
        else:
            flag = True
            for k, v in s_dic.iteritems():
                if k not in t_dic:
                    flag = False
                    break
                elif v != t_dic[k]:
                    flag = False
                    break
        return flag

if __name__ == '__main__':
    s = Solution()
    print s.isAnagram('anagram', 'nagaram')