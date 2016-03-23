"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

P     I     N
A   L S   I G
Y A   H R
P     I
convert("PAYPALISHIRING", 4) should return "PINALSIGYAHRPI".

"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        m = []
        for i in xrange(numRows):
            m.append([])
        i, j = 0, -1
        mul = 1
        first = True
        while i < len(s):
            j += mul
            m[j].append(s[i])
            if j == numRows-1:
                mul *= (-1)
            elif not first and j == 0:
                mul *= -1
            i += 1
            first = False
        n = []
        for i in m:
            n.append(''.join(i))
        return ''.join(e for e in n)

if __name__ == '__main__':
    s = Solution()
    print s.convert('PAYPALISHIRING', 4)