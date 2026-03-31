class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for c in range(9):
            for r in range(9):
                val = board[c][r]
                if val == ".": continue
                if val in cols[c] or val in rows[r] or val in squares[(c // 3, r // 3)]:
                    return False
                cols[c].add(val)
                rows[r].add(val)
                squares[(c // 3, r // 3)].add(val)

        return True