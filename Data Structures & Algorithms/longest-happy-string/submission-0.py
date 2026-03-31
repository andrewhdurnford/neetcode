class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        stack = []
        heap = []

        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))

        dup = 0      
    
        # by default -> push character with the most capacity, decrement
        # if char with most capacity = last char and dup == 2
        while heap:
            cnt0, char0 = heapq.heappop(heap)

            if not stack or char0 != stack[-1] or dup < 2:
                if stack and char0 == stack[-1]:
                    dup = 2
                else:
                    dup = 1
                stack.append(char0)
                
                if cnt0 < -1:
                    heapq.heappush(heap, (cnt0 + 1, char0))
                print(stack[-1], dup)
                continue
            
            if not heap:
                break
                
            cnt1, char1 = heapq.heappop(heap)
            stack.append(char1)
            dup = 1
            if cnt1 < -1:
                heapq.heappush(heap, (cnt1 + 1, char1))
            heapq.heappush(heap, (cnt0, char0))
            print(stack[-1], dup)
                                        
        return ''.join(stack)


                

            