class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break

        if not l <= r: return False
        li = matrix[mid]
        l = 0 
        r = len(li) - 1
        while l <= r:
            mid = (l + r) // 2
            if li[mid] < target:
                l = mid + 1
            elif li[mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
            
