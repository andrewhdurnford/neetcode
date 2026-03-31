class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l = 0
        r = rows - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        l = 0
        r = cols - 1
        nums = matrix[mid]

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: return True
            if nums[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
        
        return False

