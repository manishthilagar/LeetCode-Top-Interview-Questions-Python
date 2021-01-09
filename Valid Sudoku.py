class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for i in range(9):
            d = {}
            for j in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # Check columns
        for j in range(9):
            d = {}
            for i in range(9):
                if board[i][j] == '.':
                    pass
                elif board[i][j] in d:
                    return False
                else:
                    d[board[i][j]] = True
        # Check sub-boxes
        for m in range(0, 9, 3):
            for n in range(0, 9, 3):
                d = {}
                for i in range(n, n + 3):
                    for j in range(m, m + 3):
                        if board[i][j] == '.':
                            pass
                        elif board[i][j] in d:
                            return False
                        else:
                            d[board[i][j]] = True
        return True
