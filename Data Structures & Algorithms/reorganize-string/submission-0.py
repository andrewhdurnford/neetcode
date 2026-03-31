class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for i in range(len(s)):
            count[s[i]] += 1
        
        heap = []
        res = ""
        
        for k, v in count.items():
            heapq.heappush(heap, (-v, k))
        
        print(heap)

        cnt, char = heapq.heappop(heap)
        res += char
        if cnt < -1:
            heapq.heappush(heap, (cnt + 1, char))
        
        while heap:
            print(heap)
            if heap[0][1] != res[-1]:
                print(0)
                cnt, char = heapq.heappop(heap)
                res += char
                if cnt < -1:
                    heapq.heappush(heap, (cnt + 1, char))
            
            else:
                print(1)
                cnt0, char0 = heapq.heappop(heap)
                if not heap: return ""
                cnt, char = heapq.heappop(heap)
                res += char
                if cnt < -1:
                    heapq.heappush(heap, (cnt + 1, char))
                heapq.heappush(heap, (cnt0, char0))
        
        return res

            
