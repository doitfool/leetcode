"""
    @Project: leetcode
    @file: Valid Parentheses.py
    @author: AC
    @time: 16-5-12
    @Description:   Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.
    The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = True
        stack, top = [], -1
        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
                top += 1
            else:
                if top > -1:
                    if (stack[top] == '(' and c == ')') or (stack[top] == '[' and c == ']') or (stack[top] == '{' and c == '}'):
                        stack.pop(top)
                        top -= 1
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
        if top != -1:
            flag = False
        return flag
