class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m < n: m, n = n, m
        row = [1] * n

        for j in range(m - 1):
            new = [1] * n
            for i in range(1, n):
                new[i] = new[i - 1] + row[i]
            row = new

        return row[-1]