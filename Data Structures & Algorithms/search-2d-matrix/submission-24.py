class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        t = 0
        b = rows - 1

        while t <= b:
            m = t + ((b - t) // 2)

            if matrix[m][-1] < target:
                t = m + 1
            elif matrix[m][0] > target:
                b = m - 1
            else:
                break

        nums = matrix[t + ((b - t) // 2)]

        l = 0
        r = cols - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        
        return False
            
