class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Search for correct row
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = (l + r) // 2
            row = matrix[m]

            if row[0] <= target and row[-1] >= target:
                break
            
            elif row[-1] < target:
                l = m + 1
            
            else:
                r = m - 1
        
        l, r = 0, len(row) - 1

        while l <= r:
            m = (l + r) // 2

            if row[m] == target:
                return True
            
            elif row[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False