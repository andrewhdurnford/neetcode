class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows - 1

        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        
        if not l <= r:
            return False
        
        l, r = 0, cols - 1
        nums = matrix[mid]

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
