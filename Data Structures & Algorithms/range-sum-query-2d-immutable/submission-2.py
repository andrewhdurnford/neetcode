class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix = matrix
        
        for r in range(ROWS):
            for c in range(COLS):
                if c > 0: self.prefix[r][c] += self.prefix[r][c - 1]
                if r > 0: self.prefix[r][c] += self.prefix[r - 1][c]
                if min(r, c) > 0: 
                    self.prefix[r][c] -= self.prefix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        pre = self.prefix

        res += pre[row2][col2]
        if row1 > 0: res -= pre[row1 - 1][col2]
        if col1 > 0: res -= pre[row2][col1 - 1]
        if min(row1, col1) > 0: 
            res += pre[row1 - 1][col1 - 1]
        
        return res