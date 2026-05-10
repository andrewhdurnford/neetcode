class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = ([1, 0], [-1, 0], [0, 1], [0, -1])
        edges = set()

        for r in range(ROWS):
            if board[r][COLS - 1] == 'O':
                edges.add((r, COLS - 1))
                board[r][COLS - 1] = 'T'
            
            if board[r][0] == 'O':
                edges.add((r, 0))
                board[r][0] = 'T'
        
        for c in range(COLS):
            if board[ROWS - 1][c] == 'O':
                edges.add((ROWS - 1, c))
                board[ROWS - 1][c] = 'T'
            
            if board[0][c] == 'O':
                edges.add((0, c))
                board[0][c] = 'T'
        
        q = deque(edges)

        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (min(nr, nc) < 0
                or nr == ROWS
                or nc == COLS
                or board[nr][nc] != 'O'
                    ):
                    continue
                board[nr][nc] = 'T'
                q.append((nr, nc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] ='O'