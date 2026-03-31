class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS - 1
        row = None
        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                break

        l, r = 0, COLS - 1
        arr = matrix[m]
        while l <= r:
            m = l + ((r - l) // 2)

            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False