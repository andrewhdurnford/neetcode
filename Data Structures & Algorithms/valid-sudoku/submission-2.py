class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for row in board:
            nums = set()
            for n in row:
                if n != "." and n in nums:
                    return False
                nums.add(n)

        # Check cols (transpose to rows)
        transposed = [list(row) for row in zip(*board)]
        for col in transposed:
            nums = set()
            for n in col:
                if n != "." and n in nums:
                    return False
                nums.add(n)
        
        # Check sub-boxes
        for sq in range(9):
            nums = set()
            r = sq // 3 * 3
            c = sq % 3 * 3
            for i in range(3):
                for j in range(3):
                    n = board[i + r][j + c]
                    if n != "." and n in nums:
                        return False
                    nums.add(n)
            
        return True