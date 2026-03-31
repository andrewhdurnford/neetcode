class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        sqs = collections.defaultdict(set) #r/3,c/3

        for r in range(9):
            for c in range(9):
                i = board[r][c]
                if i == ".": continue
                if (i in rows[r] 
                or i in cols[c] 
                or i in sqs[(r // 3, c // 3)]):
                    return False
                rows[r].add(i)
                cols[c].add(i)
                sqs[(r // 3, c // 3)].add(i)
        return True
