class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # ROWS
        for r in range(9):
            found = set()
            for c in range(9):
                sq = board[r][c]
                if sq == '.': continue
                if sq in found: return False
                found.add(sq)
        
        # COLS
        for c in range(9):
            found = set()
            for r in range(9):
                sq = board[r][c]
                if sq == '.': continue
                if sq in found: return False
                found.add(sq)
        
        for i in range(9):
            found = set()
            for r in range(3):
                for c in range(3):
                    sq = board[r + (i // 3) * 3][c + (i % 3) * 3]
                    if sq == '.': continue
                    if sq in found: return False
                    found.add(sq)
        
        return True
        

