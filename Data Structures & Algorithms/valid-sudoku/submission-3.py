class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = 9, 9

        # Check cols
        for r in range(ROWS):
            numset = set()
            for c in range(9):
                if board[r][c] in numset:
                    return False
                
                if board[r][c] != '.':
                    numset.add(board[r][c])
        
        # Check rows
        for c in range(COLS):
            numset = set()
            for r in range(9):
                if board[r][c] in numset:
                    return False
                
                if board[r][c] != '.':
                    numset.add(board[r][c])
        
        # Check Squares
        for dr in range(3):
            for dc in range(3):
                numset = set()
                for sq in range(9):
                    r, c = sq // 3 + dr * 3, sq % 3 + dc * 3
                    if board[r][c] in numset:
                        return False
                    
                    if board[r][c] != '.':
                        numset.add(board[r][c])
        
        return True
