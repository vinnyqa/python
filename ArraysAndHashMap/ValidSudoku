from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        cols = defaultdict(set) #Hashmap cols, Key is column number, Value is Set contains all values in Column number
        rows = defaultdict(set) #Hashmap rows, Key is Row number, Value is Set contains all values in Row number
        squares = defaultdict(set) #HashMap squares, Key is (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True

sol = Solution()
board=[["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","1",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]
print(sol.isValidSudoku(board))
#Time: o(n2) Space: o(n2)
