class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        tasks = [-cnt for cnt in count.values()]
        heapq.heapify(tasks)

        q = deque()
        t = 0
        while tasks or q:
            t += 1
        
            if not tasks:
                t = q[0][1]
            else:
                cnt = 1 + heapq.heappop(tasks)
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                heapq.heappush(tasks, q.popleft()[0])
        
        return t
            


         
