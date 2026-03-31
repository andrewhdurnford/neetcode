class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        stack = []
        heap = []

        # use max heap
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

            if dup == 2 and char0 == stack[-1]:
                if not heap: # no character to keep string happy
                    break

                # get next char & push to stack
                cnt1, char1 = heapq.heappop(heap)
                stack.append(char1)
                dup = 1 # reset dup

                # add back chars
                if cnt1 < -1:
                    heapq.heappush(heap, (cnt1 + 1, char1))
                heapq.heappush(heap, (cnt0, char0))
                continue

            # basecase; push highest capacity char

            # dup = 1 if diff char, else 2
            if stack and char0 == stack[-1]:
                dup = 2
            else:
                dup = 1
                
            stack.append(char0)
            if cnt0 < -1:
                heapq.heappush(heap, (cnt0 + 1, char0))

        return ''.join(stack)


                

            