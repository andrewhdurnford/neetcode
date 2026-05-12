class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap tracking task count + deque tracking active cooldown
        # put tasks into dict w/ count
        # push each onto max heap (so invert count)
        # at each tick, pop top of heap, decrement in dict
        # push task to deque with the time that it will be runnable again
        # check front of deq to see if it should be added back
        
        count = defaultdict(int)
        heap = []
        # heapq.heapify(heap)
        for t in tasks:
            count[t] += 1
        for t in count.keys():
            heapq.heappush(heap, [-count[t], t])
        cooldown = deque()
        time = 0
        
        while cooldown or heap:
            time += 1

            if heap:
                _, t = heapq.heappop(heap)
                count[t] -= 1
                if count[t] > 0:
                    cooldown.append([time + n, t])
            
            if cooldown and cooldown[0][0] == time:
                    _, t = cooldown.popleft()
                    heapq.heappush(heap, [-count[t], t])
        
        return time