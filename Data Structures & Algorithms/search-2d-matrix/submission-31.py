class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # init left and right pointers
        l, r = 0, len(matrix) - 1

        # find correct row
        while l <= r:
            m = (l + r) // 2
            mid = matrix[m]

            if mid[0] <= target and mid[-1] >= target:
                break

            elif mid[0] > target:
                r = m - 1

            else:
                l = m + 1

        # check if we actually found the row -> if not, the number is not in the matrix
        if mid[0] > target or mid[-1] < target:
            return False

        arr = mid
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2
        
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False
