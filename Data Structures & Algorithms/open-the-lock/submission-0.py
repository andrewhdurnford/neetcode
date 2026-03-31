class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == '0000':
            return 0

        visit = set(deadends)

        if '0000' in visit:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        
        q = deque()
        q.append(('0000', 0))
        visit.add('0000')

        while q:
            cur, moves = q.popleft()

            if cur == target:
                return moves
                
            for child in children(cur):
                if child not in visit:
                    visit.add(child)
                    q.append((child, moves + 1))
        
        return -1