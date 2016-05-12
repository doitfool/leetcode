"""
    @Project: leetcode
    @file: Valid Sudoku.py
    @author: AC
    @time: 16-5-12
    @Description:   Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
    The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
    Note: A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        flag = True
        # rule 1
        for i in xrange(9):
            data = []
            for j in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] not in data:
                        data.append(board[i][j])
                    else:
                        flag = False
                        break
            if not flag:
                break
        # rule 2
        for j in xrange(9):
            data = []
            for i in xrange(9):
                if board[i][j] != '.':
                    if board[i][j] not in data:
                        data.append(board[i][j])
                    else:
                        flag = False
                        break
            if not flag:
                break
        # rule 3
        bounds = [[0, 0, 2, 2], [3, 0, 5, 2], [6, 0, 8, 2], [0, 3, 2, 5], [3, 3, 5, 5], [6, 3, 8, 5], [0, 6, 2, 8], [3, 6, 5, 8], [6, 6, 8, 8]]
        for i in xrange(9):
            a, b, c, d = bounds[i]
            data = []
            for r in range(a, c+1):
                for c in range(b, d+1):
                    if board[r][c] != '.':
                        if board[r][c] not in data:
                            data.append(board[r][c])
                        else:
                            flag = False
                            break
                if not flag:
                    break
            if not flag:
                break
        return flag